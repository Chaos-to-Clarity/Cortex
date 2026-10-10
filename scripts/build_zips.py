"""Check the marketplace and package every skill into an upload-ready ZIP.

Layout this expects:

    .claude-plugin/marketplace.json
    plugins/<plugin>/.claude-plugin/plugin.json
    plugins/<plugin>/skills/<skill>/SKILL.md

Each ZIP in dist/ holds one skill folder as its single top-level entry, which
is the layout Claude's "Upload a skill" expects:

    weekly-planning.zip
    └── weekly-planning/
        ├── SKILL.md
        └── references/...

Any problem fails the build, so a broken skill never reaches a release.

Usage:
    python scripts/build_zips.py
"""

import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS_DIR = ROOT / "plugins"
DIST_DIR = ROOT / "dist"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"

NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
RESERVED = ("anthropic", "claude")
DESCRIPTION_LIMIT = 200  # claude.ai upload limit
SKIP_NAMES = {".DS_Store", "Thumbs.db", "__pycache__"}


def read_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def check_skill(folder: Path) -> list:
    label = f"{folder.parent.parent.name}/{folder.name}"
    skill_md = folder / "SKILL.md"
    if not skill_md.exists():
        return [f"{label}: missing SKILL.md"]

    problems = []
    meta = read_frontmatter(skill_md)
    name = meta.get("name", "")
    description = meta.get("description", "")

    if not name:
        problems.append(f"{label}: SKILL.md has no name")
    elif name != folder.name:
        problems.append(f"{label}: name '{name}' must match the folder name")
    if name and not NAME_RE.match(name):
        problems.append(f"{label}: name must be lowercase letters, numbers, and hyphens, 64 max")
    if any(word in name for word in RESERVED):
        problems.append(f"{label}: name can't contain 'anthropic' or 'claude'")
    if not description:
        problems.append(f"{label}: SKILL.md has no description")
    elif len(description) > DESCRIPTION_LIMIT:
        problems.append(f"{label}: description is {len(description)} characters, limit {DESCRIPTION_LIMIT}")

    body = skill_md.read_text(encoding="utf-8")
    for ref in set(re.findall(r"`(references/[^`]+)`", body)):
        if not (folder / ref).exists():
            problems.append(f"{label}: mentions {ref} but the file is missing")
    return problems


def check_marketplace() -> list:
    problems = []
    try:
        market = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as err:
        return [f"marketplace.json: {err}"]

    for key in ("name", "owner", "plugins"):
        if key not in market:
            problems.append(f"marketplace.json: missing '{key}'")

    listed = set()
    for entry in market.get("plugins", []):
        name, source = entry.get("name"), entry.get("source", "")
        listed.add(name)
        plugin_dir = (ROOT / source).resolve()
        if ".." in source or not plugin_dir.is_dir():
            problems.append(f"marketplace.json: '{name}' source '{source}' is not a folder in the repo")
            continue
        manifest = plugin_dir / ".claude-plugin" / "plugin.json"
        try:
            manifest_name = json.loads(manifest.read_text(encoding="utf-8")).get("name")
        except (OSError, json.JSONDecodeError) as err:
            problems.append(f"{name}: plugin.json unreadable ({err})")
            continue
        if manifest_name != name:
            problems.append(f"{name}: plugin.json name '{manifest_name}' must match the marketplace entry")

    for folder in PLUGINS_DIR.iterdir():
        if folder.is_dir() and folder.name not in listed:
            problems.append(f"plugins/{folder.name} is not listed in marketplace.json")
    return problems


def skill_folders():
    return sorted(
        skill
        for plugin in PLUGINS_DIR.iterdir() if plugin.is_dir()
        for skill in (plugin / "skills").iterdir() if skill.is_dir()
    )


def build(folder: Path) -> Path:
    DIST_DIR.mkdir(exist_ok=True)
    out = DIST_DIR / f"{folder.name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(folder.rglob("*")):
            if path.is_dir() or any(part in SKIP_NAMES for part in path.parts):
                continue
            zf.write(path, Path(folder.name) / path.relative_to(folder))
        license_file = ROOT / "LICENSE.md"
        if license_file.exists():
            zf.write(license_file, Path(folder.name) / "LICENSE.md")
    return out


def main() -> int:
    folders = skill_folders()
    problems = check_marketplace()
    problems += [msg for folder in folders for msg in check_skill(folder)]

    seen = {}
    for folder in folders:
        if folder.name in seen:
            problems.append(f"skill name '{folder.name}' is used twice ({seen[folder.name]} and {folder.parent.parent.name})")
        seen[folder.name] = folder.parent.parent.name

    sync = subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_spec.py"), "--check"],
                          capture_output=True, text=True)
    if sync.returncode != 0:
        problems.append(sync.stdout.strip())

    if problems:
        print("Fix these before releasing:")
        for msg in problems:
            print(f"  - {msg}")
        return 1

    for folder in folders:
        print(f"Built {build(folder).relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
