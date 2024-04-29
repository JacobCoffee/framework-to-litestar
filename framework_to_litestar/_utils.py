"""Utilities for things."""

from __future__ import annotations

import inspect
from pathlib import Path
from typing import Literal


def get_absolute_path(directory: Path | str) -> str:
    """Get the absolute path of the directory."""
    return str(Path(directory).resolve())


def get_files(path: Path) -> list[Path]:
    """Get all files in the given directory."""
    return list(path.rglob("*.py"))


def get_codemods(module_name: str) -> list[str]:
    """Get all codemods from the specified module."""
    module = __import__(module_name, fromlist=[""])
    return [
        item
        for item in dir(module)
        if not item.startswith("__") and item != "modify" and inspect.isfunction(getattr(module, item))
    ]


def generate_literal_for_codemods(module_name: str) -> type:
    """Generate a Literal type for the codemods in the specified module.

    Consumed for Cappa's ``mod`` argument.
    """
    codemods = get_codemods(module_name)
    return Literal[tuple(codemods)] if codemods else Literal[None]
