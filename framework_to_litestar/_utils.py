"""Utilities for things."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


def get_absolute_path(directory: Path) -> str:
    """Get the absolute path of the directory."""
    from pathlib import Path

    return str(Path(directory).resolve())


def get_files(path: Path) -> list[Path]:
    """Get all files in the given directory."""
    return list(path.rglob("*.py"))
