"""CLI for all the modding of the codes."""

from __future__ import annotations

import sys
from dataclasses import dataclass

import cappa
from rich import get_console
from rich.traceback import install

from framework_to_litestar.frameworks.fastapi import Fastapi
from framework_to_litestar.frameworks.flask import Flask

console = get_console()
install(show_locals=True)


@dataclass
class Converter:
    """Modify code on the fly for a given web framework and directory."""

    commands: cappa.Subcommands[Fastapi | Flask]


def main() -> None:
    """Run the CLI."""
    try:
        cappa.invoke(Converter)
    except KeyboardInterrupt:
        sys.stderr.write("Exiting...\n")


if __name__ == "__main__":
    main()
