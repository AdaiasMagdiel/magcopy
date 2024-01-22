from pathlib import Path
from typing import Union

PathLike = Union[str, Path]

MAX_ITEMS_IN_CLIPBOARD = 10
CLIPBOARD_FILE = Path(__file__).parent.parent.joinpath(".clipboard").resolve()
ACTION_FILE = Path(__file__).parent.parent.joinpath(".action").resolve()


def create_files_if_not_exists() -> None:
    for file in [CLIPBOARD_FILE, ACTION_FILE]:
        if not file.is_file():
            file.touch()


def add_to_clipboard(action: str, path: PathLike) -> None:
    create_files_if_not_exists()

    path_str = path if isinstance(path, str) else path.as_posix()

    clipboard_items: list[str] = [
        item.strip()
        for item in CLIPBOARD_FILE.read_text(encoding="utf-8").split("\n")
        if item != ""
    ]
    clipboard_items.insert(0, path_str)

    if len(clipboard_items) > MAX_ITEMS_IN_CLIPBOARD:
        clipboard_items.pop()

    CLIPBOARD_FILE.write_text("\n".join(clipboard_items), encoding="utf-8")
    ACTION_FILE.write_text(action, encoding="utf-8")


def get_action() -> str:
    return ACTION_FILE.read_text(encoding="utf-8").strip()


def read_from_clipboard() -> Path:
    clipboard_items: list[str] = [
        item.strip()
        for item in CLIPBOARD_FILE.read_text().split("\n")
        if item != ""
    ]

    return Path(clipboard_items[0])
