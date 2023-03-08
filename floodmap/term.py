import os
from rich.console import Console
from typing import Any


def vprint(x: Any, verbose: bool = True) -> None:
    if verbose:
        Console().print(x)


def clear():
    os.system("cls" if os.name == "nt" else "clear")
