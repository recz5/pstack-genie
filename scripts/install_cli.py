#!/usr/bin/env python3
"""Optional local Genie Code CLI skill install; no automatic overwrites."""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '.agents' / 'skills'


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', type=Path, default=Path.home() / '.genie' / 'skills')
    parser.add_argument('--force', action='store_true', help='Replace existing copies of these skills')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    destination = args.destination.expanduser().resolve()
    skills = sorted(p for p in SOURCE.iterdir() if (p / 'SKILL.md').is_file())
    if not skills:
        raise SystemExit('No skills found')
    existing = [p.name for p in skills if (destination / p.name).exists()]
    if existing and not args.force:
        raise SystemExit(f'Existing destination skills: {", ".join(existing)}. Use --force only after review.')
    for source in skills:
        target = destination / source.name
        print(f'{source} -> {target}' + (' [dry-run]' if args.dry_run else ''))
        if args.dry_run:
            continue
        destination.mkdir(parents=True, exist_ok=True)
        if target.exists():
            if target.is_dir() and not target.is_symlink():
                shutil.rmtree(target)
            else:
                target.unlink()
        shutil.copytree(source, target)
    if not args.dry_run:
        print('Installed. Start a fresh Genie Code CLI session to load the updated skills.')


if __name__ == '__main__':
    main()
