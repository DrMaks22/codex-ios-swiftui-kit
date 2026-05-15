#!/usr/bin/env python3
"""Install the Codex iOS SwiftUI kit into a local Codex plugin directory."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PLUGIN_NAME = "codex-ios-swiftui-kit"
PLUGIN_CATEGORY = "Productivity"
INSTALLATION_POLICY = "AVAILABLE"
AUTHENTICATION_POLICY = "ON_INSTALL"
DEFAULT_MARKETPLACE_NAME = "local"
DEFAULT_MARKETPLACE_DISPLAY_NAME = "Local Plugins"
REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PLUGIN_ROOT = REPO_ROOT / "plugins" / PLUGIN_NAME
DEFAULT_TARGET_ROOT = Path.home() / "plugins"
DEFAULT_MARKETPLACE_PATH = Path.home() / ".agents" / "plugins" / "marketplace.json"
VALID_SCOPES = {"global", "local"}


@dataclass(frozen=True)
class InstallConfig:
    scope: str
    workspace_root: Path | None
    target_root: Path | None
    marketplace_path: Path | None
    force: bool
    link: bool
    dry_run: bool
    skip_marketplace: bool
    skip_validation: bool


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def atomic_write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        delete=False,
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
    ) as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
        temp_path = Path(handle.name)
    temp_path.replace(path)


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
        return
    if path.is_dir():
        shutil.rmtree(path)
        return
    path.unlink(missing_ok=True)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def detect_workspace_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        candidate = Path(result.stdout.strip())
        if candidate:
            return candidate.expanduser()
    return Path.cwd().expanduser()


def resolve_install_paths(config: InstallConfig) -> tuple[Path, Path]:
    if config.scope == "global":
        target_root = DEFAULT_TARGET_ROOT
        marketplace_path = DEFAULT_MARKETPLACE_PATH
    elif config.scope == "local":
        workspace_root = config.workspace_root or detect_workspace_root()
        workspace_root = workspace_root.expanduser()
        if workspace_root.exists() and not workspace_root.is_dir():
            raise ValueError(f"Workspace root must be a directory: {workspace_root}")
        if workspace_root.resolve() == REPO_ROOT.resolve():
            raise ValueError(
                "Local scope cannot target the source repository itself. "
                "Pass --workspace-root /path/to/the workspace you want Codex to install into."
            )
        target_root = workspace_root / "plugins"
        marketplace_path = workspace_root / ".agents" / "plugins" / "marketplace.json"
    else:
        raise ValueError(f"Unsupported scope: {config.scope}")

    if config.target_root is not None:
        target_root = config.target_root.expanduser()
    if config.marketplace_path is not None:
        marketplace_path = config.marketplace_path.expanduser()

    return target_root, marketplace_path


def validate_source_bundle(source_root: Path) -> None:
    manifest_path = source_root / ".codex-plugin" / "plugin.json"
    require(source_root.is_dir(), f"Source plugin root is missing: {source_root}")
    require(manifest_path.is_file(), f"Missing plugin manifest: {manifest_path}")

    manifest = load_json(manifest_path)
    require(isinstance(manifest, dict), "plugin.json must contain a JSON object.")
    require(
        manifest.get("name") == PLUGIN_NAME,
        f"plugin.json name must be '{PLUGIN_NAME}'.",
    )

    skills_path = source_root / "skills"
    require(skills_path.is_dir(), f"Missing skills directory: {skills_path}")
    skill_dirs = [path for path in sorted(skills_path.iterdir()) if path.is_dir()]
    require(skill_dirs, "The bundle does not contain any skill directories.")

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        agents_yaml = skill_dir / "agents" / "openai.yaml"
        require(skill_md.is_file(), f"Missing skill file: {skill_md}")
        require(agents_yaml.is_file(), f"Missing skill agent metadata: {agents_yaml}")

    assets_path = source_root / "assets"
    require(assets_path.is_dir(), f"Missing assets directory: {assets_path}")
    for asset_name in ("icon.svg", "logo.svg"):
        asset_path = assets_path / asset_name
        require(asset_path.is_file(), f"Missing asset: {asset_path}")

    mcp_path = source_root / ".mcp.json"
    if mcp_path.exists():
        mcp_payload = load_json(mcp_path)
        require(isinstance(mcp_payload, dict), ".mcp.json must contain a JSON object.")


def validate_installed_bundle(plugin_root: Path) -> None:
    validate_source_bundle(plugin_root)


def build_marketplace_entry() -> dict[str, Any]:
    return {
        "name": PLUGIN_NAME,
        "source": {
            "source": "local",
            "path": f"./plugins/{PLUGIN_NAME}",
        },
        "policy": {
            "installation": INSTALLATION_POLICY,
            "authentication": AUTHENTICATION_POLICY,
        },
        "category": PLUGIN_CATEGORY,
    }


def load_or_initialize_marketplace(path: Path) -> dict[str, Any]:
    if path.exists():
        payload = load_json(path)
        require(isinstance(payload, dict), f"{path} must contain a JSON object.")
    else:
        payload = {
            "name": DEFAULT_MARKETPLACE_NAME,
            "interface": {
                "displayName": DEFAULT_MARKETPLACE_DISPLAY_NAME,
            },
            "plugins": [],
        }

    payload.setdefault("name", DEFAULT_MARKETPLACE_NAME)
    interface = payload.get("interface")
    if interface is None:
        interface = {}
        payload["interface"] = interface
    else:
        require(isinstance(interface, dict), f"{path} field 'interface' must be an object.")
    interface.setdefault("displayName", DEFAULT_MARKETPLACE_DISPLAY_NAME)

    plugins = payload.get("plugins")
    if plugins is None:
        plugins = []
        payload["plugins"] = plugins
    require(isinstance(plugins, list), f"{path} field 'plugins' must be an array.")

    return payload


def merge_marketplace_entry(path: Path, dry_run: bool) -> bool:
    payload = load_or_initialize_marketplace(path)
    entry = build_marketplace_entry()
    plugins = payload["plugins"]

    for index, current in enumerate(plugins):
        if isinstance(current, dict) and current.get("name") == PLUGIN_NAME:
            if current == entry:
                return False
            plugins[index] = entry
            if not dry_run:
                atomic_write_json(path, payload)
            return True

    plugins.append(entry)
    if not dry_run:
        atomic_write_json(path, payload)
    return True


def sync_tree(source_root: Path, target_root: Path, *, force: bool, link: bool, dry_run: bool) -> str:
    target_parent = target_root.parent
    if dry_run:
        action = "link" if link else "copy"
        return f"Would {action} {source_root} -> {target_root}"

    target_parent.mkdir(parents=True, exist_ok=True)

    if link:
        if target_root.exists() or target_root.is_symlink():
            if not force:
                if target_root.is_symlink() and target_root.resolve() == source_root.resolve():
                    return f"Already linked at {target_root}"
                raise FileExistsError(
                    f"Target already exists: {target_root}. Use --force to replace it."
                )
            remove_path(target_root)
        target_root.symlink_to(source_root, target_is_directory=True)
        return f"Linked {target_root} -> {source_root}"

    if target_root.exists() or target_root.is_symlink():
        if not target_root.is_dir() or target_root.is_symlink():
            if not force:
                raise FileExistsError(
                    f"Target already exists and is not a directory: {target_root}. "
                    "Use --force to replace it."
                )
            remove_path(target_root)
            shutil.copytree(source_root, target_root)
            return f"Copied fresh bundle to {target_root}"

        if force:
            remove_path(target_root)
            shutil.copytree(source_root, target_root)
            return f"Copied fresh bundle to {target_root}"

        shutil.copytree(source_root, target_root, dirs_exist_ok=True)
        return f"Updated existing bundle at {target_root}"

    shutil.copytree(source_root, target_root)
    return f"Copied bundle to {target_root}"


def parse_args() -> InstallConfig:
    parser = argparse.ArgumentParser(
        description="Install the Codex iOS SwiftUI kit into a local Codex plugin directory.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--scope",
        choices=sorted(VALID_SCOPES),
        default="global",
        help="Install into the global Codex profile or into a specific workspace.",
    )
    parser.add_argument(
        "--workspace-root",
        default=None,
        help="Target workspace root for local installs.",
    )
    parser.add_argument(
        "--target-root",
        default=None,
        help="Override the parent directory for the installed plugin bundle.",
    )
    parser.add_argument(
        "--marketplace-path",
        default=None,
        help="Override the Codex marketplace manifest path that should be updated.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing plugin directory or symlink instead of updating in place.",
    )
    parser.add_argument(
        "--link",
        action="store_true",
        help="Install as a symlink to the repository copy instead of copying files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the planned actions without writing any files.",
    )
    parser.add_argument(
        "--skip-marketplace",
        action="store_true",
        help="Install the bundle without touching the marketplace manifest.",
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Skip structural validation after installation.",
    )
    args = parser.parse_args()
    return InstallConfig(
        scope=args.scope,
        workspace_root=Path(args.workspace_root).expanduser() if args.workspace_root else None,
        target_root=Path(args.target_root).expanduser() if args.target_root else None,
        marketplace_path=Path(args.marketplace_path).expanduser() if args.marketplace_path else None,
        force=args.force,
        link=args.link,
        dry_run=args.dry_run,
        skip_marketplace=args.skip_marketplace,
        skip_validation=args.skip_validation,
    )


def main() -> int:
    config = parse_args()

    try:
        validate_source_bundle(SOURCE_PLUGIN_ROOT)
        target_root, marketplace_path = resolve_install_paths(config)

        target_plugin_root = target_root / PLUGIN_NAME
        print(
            sync_tree(
                SOURCE_PLUGIN_ROOT,
                target_plugin_root,
                force=config.force,
                link=config.link,
                dry_run=config.dry_run,
            )
        )

        if not config.skip_marketplace:
            changed = merge_marketplace_entry(marketplace_path, config.dry_run)
            if config.dry_run:
                print(f"Would update marketplace at {marketplace_path}")
            elif changed:
                print(f"Updated marketplace at {marketplace_path}")
            else:
                print(f"Marketplace already contained {PLUGIN_NAME}")

        if not config.skip_validation and not config.dry_run:
            validate_installed_bundle(target_plugin_root)
            print(f"Validated installed bundle at {target_plugin_root}")

        if config.dry_run:
            print("Dry run complete. No files were changed.")
        else:
            print("Installation complete.")
            print(
                "Open Codex, refresh plugins, and the bundle should appear under the local marketplace."
            )
        return 0
    except (OSError, ValueError, json.JSONDecodeError, FileExistsError) as exc:
        print(f"install failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
