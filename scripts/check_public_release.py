#!/usr/bin/env python3
"""Lightweight working-tree checks before public release; NOT a full secret scan."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {'.git', '.venv', '__pycache__', '.pytest_cache'}
EXCLUDED_FILES = {'check_public_release.py', 'test_public_release.py'}
BLOCKED_NAMES = {'.env', '.databrickscfg', 'credentials.json', 'id_rsa', 'id_ed25519'}
PATTERNS = [
    ('private key', re.compile(r'-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----')),
    ('alternate Git provider token', re.compile(r'glpat-[A-Za-z0-9_-]{16,}')),
    ('GitHub token', re.compile(r'(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{22,})')),
    ('Databricks PAT', re.compile(r'dapi[0-9a-f]{32}', re.IGNORECASE)),
    ('AWS access key', re.compile(r'AKIA[0-9A-Z]{16}')),
]


def check_public_release(root: Path = ROOT) -> list[str]:
    problems: list[str] = []
    for path in sorted(root.rglob('*')):
        if not path.is_file() or any(part in EXCLUDED_DIRS for part in path.relative_to(root).parts):
            continue
        if path.name in EXCLUDED_FILES:
            continue
        if path.name in BLOCKED_NAMES or (path.name.startswith('.env.') and path.name != '.env.example'):
            problems.append(f'{path.relative_to(root)}: sensitive-looking filename')
            continue
        if path.stat().st_size > 2_000_000:
            continue
        try:
            body = path.read_text(encoding='utf-8')
        except (UnicodeError, OSError):
            continue
        for name, pattern in PATTERNS:
            if pattern.search(body):
                problems.append(f'{path.relative_to(root)}: possible {name} (value redacted)')
    return problems


def main() -> None:
    problems = check_public_release()
    if problems:
        raise SystemExit('\n'.join(problems))
    print('PASS: no obvious secrets in working-tree text files; scan full Git history separately')


if __name__ == '__main__':
    main()
