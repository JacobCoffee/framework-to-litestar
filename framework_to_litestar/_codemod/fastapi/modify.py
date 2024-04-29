"""Modify files based on specified codemods and directory.

Currently does a vary naive string transformation, will look to using
`bowler` or `libCST` directly in the future.
"""

from __future__ import annotations

from pathlib import Path

from rich import get_console

from framework_to_litestar._codemod.fastapi.app import transform_app_initialization
from framework_to_litestar._codemod.fastapi.decorators import transform_decorators
from framework_to_litestar._utils import get_absolute_path, get_files

console = get_console()


def modify_file(file_path: Path, mods: list[str] | None, dry_run: bool = False) -> None:
    """Modify a single file based on specified codemods.

    Args:
        file_path (Path): The path to the file to modify.
        mods (list[str] | None): List of codemods to apply, apply all if None.
        dry_run (bool): Perform a dry run without modifying the file.
    """
    with file_path.open() as file:
        code = file.read()

    if mods is None or "decorators" in mods:
        code = transform_decorators(code)
    if mods is None or "app" in mods:
        code = transform_app_initialization(code)

    if not dry_run:
        with file_path.open("w") as file:
            file.write(code)


def modify_files(directory: Path | str, mods: list[str] | None, dry_run: bool = False) -> None:
    """Modify all files in the given directory based on specified codemods.

    Args:
        directory (Path): The directory to modify.
        mods (list[str] | None): List of codemods to apply, apply all if None.
        dry_run (bool): Perform a dry run without modifying files.
    """
    console.print(f"Modifying files in '{get_absolute_path(directory)}'")
    for file_path in get_files(Path(directory)):
        msg = f"Would have modified file '{file_path}'" if dry_run else f"Modifying file '{file_path}'"
        console.print(msg)
        modify_file(file_path, mods, dry_run)


if __name__ == "__main__":
    # Example usage while running this file directly. Only runs `decorators` codemod.
    directory = Path("examples")
    mods = ["decorators"]
    modify_files(directory, mods)
