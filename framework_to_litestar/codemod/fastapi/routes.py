# framework_to_litestar/codemod.py
from __future__ import annotations

from pathlib import Path

from bowler import Query
from rich import get_console

from framework_to_litestar._utils import get_absolute_path, get_files

console = get_console()


def transform_decorator(node, capture, filename) -> None:
    """Transform FastAPI decorators to a Litestar decorator.

    Args:
        ...
    """
    raise NotImplementedError("This function is not implemented yet.")


def modify_files(directory: Path) -> None:
    """Modify all files in the given directory.

    .. todo:: This doesn't work yet.

    Args:
        directory (Path): The directory to modify.
    """
    console.print(f"Modifying files in '{get_absolute_path(directory)}'")
    for file_path in get_files(Path(directory)):
        console.print(f"Modifying file '{file_path}'")
        q = Query(str(file_path))
        (((q.select_module("app")
           .modify(transform_decorator))
          .diff(interactive=True))
         .execute(write=True, interactive=False))
