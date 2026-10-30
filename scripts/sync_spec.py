"""Copy the spec files into every Cortex skill's references/ folder.

Plugins install as self-contained copies and single-skill ZIPs must stand
alone, so each skill carries its own copy of each spec file. Edit the masters
in spec/, then run this.

Files copied:
    spec/cortex-spec.md   the core spec, into every Cortex skill
    spec/company-pack.md  the Company Pack, into every Cortex skill

Usage:
    python scripts/sync_spec.py          # copy
    python scripts/sync_spec.py --check  # fail if any copy is out of date
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC_FILES = [ROOT / "spec" / "cortex-spec.md", ROOT / "spec" / "company-pack.md"]
SKILLS = ROOT / "plugins" / "cortex" / "skills"


def main() -> int:
    check = "--check" in sys.argv
    stale = []
    for spec in SPEC_FILES:
        master = spec.read_text(encoding="utf-8")
        for skill in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
            dest = skill / "references" / spec.name
            if dest.exists() and dest.read_text(encoding="utf-8") == master:
                continue
            if check:
                stale.append(dest.relative_to(ROOT))
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(master, encoding="utf-8")
                print(f"Updated {dest.relative_to(ROOT)}")
    if stale:
        print("Spec copies out of date. Run: python scripts/sync_spec.py")
        for path in stale:
            print(f"  - {path}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
