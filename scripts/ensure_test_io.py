#!/usr/bin/env python3
"""Ensure every section cpp/ and py/ folder has data.in and data.out."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def ensure_test_io_files(root: Path = ROOT) -> int:
    created = 0
    for folder in sorted(root.glob("[0-9]*_*")):
        if not folder.is_dir():
            continue
        for sub in ("cpp", "py"):
            lang_dir = folder / sub
            lang_dir.mkdir(parents=True, exist_ok=True)
            for name in ("data.in", "data.out"):
                path = lang_dir / name
                if not path.exists():
                    path.touch()
                    created += 1
    return created


def main() -> None:
    created = ensure_test_io_files()
    print(f"Created {created} test I/O files")


if __name__ == "__main__":
    main()
