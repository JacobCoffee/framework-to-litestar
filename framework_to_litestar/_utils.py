"""Utilities for things."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Literal

from rich import get_console

from framework_to_litestar.exceptions import CodemodeNotFoundError

console = get_console()


def get_absolute_path(directory: Path | str) -> str:
    """Get the absolute path of the directory."""
    return str(Path(directory).resolve())


def get_files(path: Path) -> list[Path]:
    """Get all files in the given directory."""
    # check if path exists
    if not path.exists():
        console.print(f"Path '{path}' does not exist", style="red")
        sys.exit(1)
    return list(path.rglob("*.py"))


def get_codemods(module_name: str) -> list[str]:
    """Get all codemods from the specified module."""
    try:
        module = __import__(module_name, fromlist=[""])
        if codemods := [item for item in dir(module) if not item.startswith("__") and item != "modify"]:
            return codemods
        msg = f"No codemods found in module '{module_name}'"
        raise CodemodeNotFoundError(msg)
    except ImportError as e:
        msg = f"Module '{module_name}' not found"
        raise CodemodeNotFoundError(msg) from e


def generate_options_for_codemods(module_name: str) -> Literal[tuple[str, ...]] | None:
    """Generate a Literal type for the codemods in the specified module.

    Consumed for Cappa's ``mod`` argument.
    """
    try:
        if codemods := get_codemods(module_name):
            return Literal[tuple(codemods)]
    except CodemodeNotFoundError:
        console.print(f"No codemods found in module '{module_name}'", style="red")
        sys.exit(1)
