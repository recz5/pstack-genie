#!/usr/bin/env python3
"""Safely vendor original cursor/plugins pstack without replacing Genie Code adapters.

This script requires git and network access, unless --from-dir points to an
existing local checkout containing the pstack directory.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import tempfile

REPO = 'https://github.com/cursor/plugins.git'
ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'vendor' / 'pstack'


def execute(args: list[str], *, cwd: Path | None = None) -> str:
    return subprocess.check_output(args, cwd=cwd, text=True, stderr=subprocess.STDOUT).strip()


def vendor_from_checkout(checkout: Path, dest: Path, *, revision: str = 'unknown') -> None:
    """Copy public pstack files. Never follow symlinks or run upstream code."""
    source = checkout / 'pstack'
    if not (source / 'skills' / 'poteto-mode' / 'SKILL.md').is_file():
        raise RuntimeError(f'Missing upstream pstack/skills/poteto-mode/SKILL.md in {checkout}')
    if not (source / 'LICENSE').is_file():
        raise RuntimeError('Upstream LICENSE missing; refusing import')
    if dest.exists():
        raise RuntimeError(f'{dest} already exists. Remove deliberately before importing again.')
    # Reject symlinks before copying third-party files into the local repository.
    if any(p.is_symlink() for p in source.rglob('*')):
        raise RuntimeError('Upstream checkout contains symlinks; manual review required')
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, dest, symlinks=False, ignore=shutil.ignore_patterns('.git', '__pycache__', '*.pyc'))
    (dest.parent / 'UPSTREAM.txt').write_text(
        f'Source: {REPO}\nSubdirectory: pstack\nRevision: {revision}\n'
        'License: MIT. See pstack/LICENSE for the original copyright and license.\n'
        'Original content was copied unchanged. Active Genie Code skills are under .agents/skills/.\n',
        encoding='utf-8',
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--from-dir', type=Path, help='Existing cursor/plugins checkout root')
    parser.add_argument('--destination', type=Path, default=DEST, help='Destination pstack directory')
    args = parser.parse_args()
    if args.from_dir:
        checkout = args.from_dir.expanduser().resolve()
        try:
            sha = execute(['git', 'rev-parse', 'HEAD'], cwd=checkout)
        except (OSError, subprocess.CalledProcessError):
            sha = 'local checkout; revision not available'
        vendor_from_checkout(checkout, args.destination.resolve(), revision=sha)
    else:
        with tempfile.TemporaryDirectory(prefix='poteto-upstream-') as temp:
            checkout = Path(temp) / 'cursor-plugins'
            execute(['git', 'clone', '--depth', '1', '--filter=blob:none', '--sparse', REPO, str(checkout)])
            execute(['git', 'sparse-checkout', 'set', 'pstack'], cwd=checkout)
            sha = execute(['git', 'rev-parse', 'HEAD'], cwd=checkout)
            vendor_from_checkout(checkout, args.destination.resolve(), revision=sha)
    print(f'Imported upstream pstack at {args.destination.resolve()}')
    print('Review vendor/pstack before adapting additional skills. The active mode was not overwritten.')


if __name__ == '__main__':
    main()
