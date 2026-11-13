#!/usr/bin/env python3
"""Dependency-free checks for portable Agent Skills and relative markdown references."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.agents' / 'skills'
LINK = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
NAME = re.compile(r'^name:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$', re.MULTILINE)
DESCRIPTION = re.compile(r'^description:\s*(\S.+)\s*$', re.MULTILINE)


def validate_skills(root: Path = SKILLS) -> list[str]:
    errors: list[str] = []
    entries = sorted(root.glob('*/SKILL.md'))
    if not entries:
        return [f'No Agent Skills found under {root}']
    for entry in entries:
        body = entry.read_text(encoding='utf-8')
        if not body.startswith('---\n') or '\n---\n' not in body[4:]:
            errors.append(f'{entry}: malformed YAML frontmatter')
            continue
        frontmatter = body.split('---', 2)[1]
        name = NAME.search(frontmatter)
        if not name or name.group(1) != entry.parent.name:
            errors.append(f'{entry}: missing/incorrect name')
        if not DESCRIPTION.search(frontmatter):
            errors.append(f'{entry}: missing description')
        for document in [entry, *sorted((entry.parent / 'references').rglob('*.md'))] if (entry.parent / 'references').exists() else [entry]:
            content = document.read_text(encoding='utf-8')
            for dest in LINK.findall(content):
                target = dest.split('#', 1)[0]
                if not target or '://' in target or target.startswith('mailto:'):
                    continue
                if not (document.parent / target).exists():
                    errors.append(f'{document}: broken reference {dest}')
    return errors


def main() -> None:
    errors = validate_skills()
    if errors:
        raise SystemExit('\n'.join(errors))
    print('PASS: skills discovered, frontmatter valid, local references resolve')


if __name__ == '__main__':
    main()
