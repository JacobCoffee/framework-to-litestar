from __future__ import annotations

from dataclasses import dataclass

import cappa
from rich import get_console
from rich.panel import Panel
from rich.progress import Progress
from rich.prompt import Confirm
from typing_extensions import Annotated, Doc

from framework_to_litestar.codemod.fastapi.routes import modify_files
from framework_to_litestar.utils import get_absolute_path

console = get_console()


@cappa.command(invoke="framework_to_litestar.frameworks.fastapi.convert")
@dataclass
class Fastapi:
    """Arguments for the FastAPI conversion command."""
    directory: Annotated[str, cappa.Arg(help="Directory to convert")]
    dry_run: Annotated[bool, cappa.Arg(help="Perform a dry run without modifying files")] = False
    confirm: Annotated[bool | None, cappa.Arg(long=True), Doc("Confirm before proceeding with the conversion")] = None


def convert(command: Fastapi) -> None:
    """Convert FastAPI route methods to Litestar style."""
    target_directory = command.directory

    console.print(Panel("FastAPI to Litestar Converter", expand=False))
    console.rule("Conversion Details")
    console.print(f"Directory: '{get_absolute_path(target_directory)}'")

    if command.confirm is None:
        command.confirm = Confirm.ask("Do you want to proceed with the conversion?")

    if not command.confirm:
        console.print("Conversion aborted.", style="yellow")
        return

    with Progress() as progress:
        task = progress.add_task("Converting files...", total=100)

        try:
            modify_files(command.directory)
            progress.update(task, completed=100)
            console.print("Conversion completed successfully!", style="green")
        except Exception as e:  # noqa: BLE001
            progress.stop()
            console.print(f"Conversion failed: {e!s}", style="red")
