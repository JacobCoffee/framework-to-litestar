from __future__ import annotations

from dataclasses import dataclass

import cappa
from typing_extensions import Annotated, Doc


@dataclass
class Flask:
    """Arguments for the FastAPI conversion command."""

    directory: Annotated[str, cappa.Arg(help="Directory to convert")]
    dry_run: Annotated[bool, cappa.Arg(help="Perform a dry run without modifying files")] = False
    confirm: Annotated[bool | None, cappa.Arg(long=True), Doc("Confirm before proceeding with the conversion")] = None
