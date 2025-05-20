import sys
from pathlib import Path
from typing import Union


def asset(path: Union[Path, str] = "") -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS).joinpath("assets", path)

    return Path().cwd().joinpath("examples", "assets", path)
