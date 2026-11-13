
#!/usr/bin/env python3
"""
Rename the locally maintained Genie Code skill.

Usage:
    python3 scripts/rename_skill.py ube-mode
    python3 scripts/rename_skill.py ube-mode --apply
    python3 scripts/rename_skill.py mango-mode --from ube-mode --apply

Dry-run by default. Does not commit, push, or deploy.
Preserves vendored upstream files.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

DEFAULT_OLD = "poteto-mode"
DEFAULT_NEW = "ube-mode"

SKILL_NAME_PATTERN = re.compile(
    r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
)

SKILL_PARENT = Path(".agents/skills")

SKIP_DIRS = {
    ".git",
    "vendor",
    "node_modules",
    ".next",
    ".venv",
    "venv",
    "dist",
    "build",
    "coverage",
    ".yarn",
    "__pycache__",
    ".pytest_cache",
}

TEXT_SUFFIXES = {
    ".md", ".mdx", ".txt",
    ".yaml", ".yml", ".json", ".jsonc",
    ".py", ".toml", ".ini", ".cfg",
    ".sh", ".bash", ".ps1",
    ".js", ".mjs", ".cjs",
    ".ts", ".tsx", ".jsx",
    ".html", ".xml",
}

MAX_FILE_SIZE = 2 * 1024 * 1024

# These files describe the original upstream import.
PRESERVE_FILES = {
    Path("scripts/import_upstream.py"),
    Path("tests/test_import_upstream.py"),
}

# Preserve upstream paths embedded in documentation.
UPSTREAM_PATH = re.compile(
    r"(?<![\w/\\])vendor[/\\]pstack[/\\][^\s`|<>)\]}]+",
    re.I,
)

# The porting matrix identifies original upstream skills.
UPSTREAM_TABLE_ENTRY = re.compile(
    r"(?m)^(\s*\|\s*`?)poteto-mode(`?\s*\|)",
    re.I,
)


def git(root: Path, *args: str) -> bytes:
    proc = subprocess.run(
        ["git", *args],
        cwd=root,
        capture_output=True,
    )

    if proc.returncode:
        raise RuntimeError(
            f"git {' '.join(args)} failed: "
            + proc.stderr.decode(
                "utf-8", "replace"
            ).strip()
        )

    return proc.stdout


def repository_root() -> Path:
    proc = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
    )

    if proc.returncode:
        raise RuntimeError(
            "Run this inside the pstack-genie Git repository."
        )

    return Path(proc.stdout.strip()).resolve()


def replacement(
    match: re.Match[str],
    value: str,
) -> str:
    original = match.group()

    if original.isupper():
        return value.upper()

    if original == original.title():
        return value.title()

    if original[0].isupper():
        return value[0].upper() + value[1:]

    return value


def camel_case(name: str) -> str:
    head, *tail = name.split("-")

    return head + "".join(
        part.capitalize()
        for part in tail
    )


def rename_text(
    value: str,
    is_porting_matrix: bool,
    old: str,
    new: str,
) -> str:
    shields: list[str] = []

    def shield(match: re.Match[str]) -> str:
        shields.append(match.group())

        return (
            f"\x00UPSTREAM_{len(shields) - 1}\x00"
        )

    value = UPSTREAM_PATH.sub(shield, value)

    if is_porting_matrix:
        value = UPSTREAM_TABLE_ENTRY.sub(
            lambda m: (
                f"{m.group(1)}"
                "\x00UPSTREAM_NAME\x00"
                f"{m.group(2)}"
            ),
            value,
        )

    forms = [
        (old, new),
        (
            old.replace("-", "_"),
            new.replace("-", "_"),
        ),
        (
            old.replace("-", " "),
            new.replace("-", " "),
        ),
        (
            camel_case(old),
            camel_case(new),
        ),
    ]

    for original, destination in forms:
        value = re.sub(
            re.escape(original),
            lambda m, dest=destination: replacement(
                m, dest
            ),
            value,
            flags=re.I,
        )

    if is_porting_matrix:
        value = value.replace(
            "\x00UPSTREAM_NAME\x00",
            "poteto-mode",
        )

    for index, item in enumerate(shields):
        value = value.replace(
            f"\x00UPSTREAM_{index}\x00",
            item,
        )

    return value


def candidate_files(root: Path) -> list[Path]:
    names = git(
        root,
        "ls-files",
        "-co",
        "--exclude-standard",
        "-z",
    ).split(b"\x00")

    results = []
    seen = set()

    for raw in names:
        if not raw:
            continue

        relative = Path(
            raw.decode(
                "utf-8",
                "surrogateescape",
            )
        )

        if (
            relative in seen
            or relative in PRESERVE_FILES
            or (root / relative).resolve()
            == Path(__file__).resolve()
            or any(
                part in SKIP_DIRS
                for part in relative.parts
            )
        ):
            continue

        seen.add(relative)
        path = root / relative

        if (
            not path.is_file()
            or path.stat().st_size > MAX_FILE_SIZE
        ):
            continue

        if (
            path.suffix.lower() in TEXT_SUFFIXES
            or path.name in {
                "Dockerfile",
                "Makefile",
                ".gitignore",
                ".gitattributes",
            }
        ):
            results.append(relative)

    return sorted(results)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__
    )

    parser.add_argument(
        "new_name",
        nargs="?",
        default=DEFAULT_NEW,
        help=(
            f"New skill name "
            f"(default: {DEFAULT_NEW})"
        ),
    )

    parser.add_argument(
        "--from",
        dest="old_name",
        default=DEFAULT_OLD,
        help=(
            f"Current skill name "
            f"(default: {DEFAULT_OLD})"
        ),
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually rename and edit files",
    )

    args = parser.parse_args()

    old = args.old_name
    new = args.new_name

    for label, name in (
        ("Source", old),
        ("Destination", new),
    ):
        if not SKILL_NAME_PATTERN.fullmatch(name):
            parser.error(
                f"{label} skill name must be "
                f"lowercase kebab-case: {name!r}"
            )

    if old == new:
        parser.error(
            "Source and destination must differ"
        )

    root = repository_root()

    old_dir = root / SKILL_PARENT / old
    new_dir = root / SKILL_PARENT / new

    if not old_dir.is_dir():
        raise RuntimeError(
            f"Missing skill folder: {old_dir}"
        )

    if new_dir.exists():
        raise RuntimeError(
            f"Destination already exists: {new_dir}"
        )

    skill_file = old_dir / "SKILL.md"

    if not skill_file.is_file():
        raise RuntimeError(
            f"Missing skill entrypoint: {skill_file}"
        )

    # Prepare all text changes before modifying files.
    changes: list[tuple[Path, bytes]] = []

    for relative in candidate_files(root):
        path = root / relative
        before = path.read_bytes()

        try:
            decoded = before.decode("utf-8")
        except UnicodeDecodeError:
            continue

        changed = rename_text(
            decoded,
            relative.as_posix()
            == "docs/PSTACK_PORTING_MATRIX.md",
            old,
            new,
        )

        after = changed.encode("utf-8")

        if after != before:
            changes.append(
                (relative, after)
            )

    new_skill_text = rename_text(
        skill_file.read_text(encoding="utf-8"),
        False,
        old,
        new,
    )

    frontmatter = new_skill_text.split(
        "---", 2
    )

    if (
        len(frontmatter) < 3
        or not re.search(
            rf"(?m)^name:\s*['\"]?"
            rf"{re.escape(new)}"
            rf"['\"]?\s*$",
            frontmatter[1],
        )
    ):
        raise RuntimeError(
            f"Renamed SKILL.md must declare "
            f"'name: {new}'"
        )

    print(f"Repository: {root}")

    print(
        f"Skill folder: "
        f"{SKILL_PARENT / old}"
        f" -> {SKILL_PARENT / new}"
    )

    print(
        f"Text files to update: {len(changes)}"
    )

    for relative, _ in changes:
        print("  ", relative)

    print(
        "Excluded: vendor/, "
        "upstream import files, this script, "
        "and binary files"
    )

    if not args.apply:
        print(
            "\nDRY RUN. No changes made."
        )
        print(
            "Run with --apply to execute."
        )
        return 0

    # Rename using Git so history is preserved.
    git(
        root,
        "mv",
        "--",
        (SKILL_PARENT / old).as_posix(),
        (SKILL_PARENT / new).as_posix(),
    )

    # Apply reference updates.
    for relative, after in changes:
        if relative.parts[:3] == (
            ".agents",
            "skills",
            old,
        ):
            target = (
                SKILL_PARENT
                / new
                / relative.relative_to(
                    SKILL_PARENT / old
                )
            )
        else:
            target = relative

        (root / target).write_bytes(after)

    print("\nRename applied successfully.")

    print(
        "Review with:"
        "\n  git status --short"
        "\n  git diff HEAD --stat"
    )

    print(
        "Run repository validation "
        "before committing."
    )

    print(
        "Update the separate Genie Code "
        "web installation if applicable."
    )

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())

    except (RuntimeError, OSError) as error:
        print(
            f"ERROR: {error}",
            file=sys.stderr,
        )
        raise SystemExit(1)
