"""Descarga los recursos de referencia del curso en ./recursos/."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPOS: dict[str, str] = {
  "architecture-patterns": "https://turan-edu.uz/media/books/2025/01/15/Architecture-Patterns-with-Python.pdf",
  "beyond-the-basic-stuff": "https://dn721805.ca.archive.org/0/items/ebooks_202307/beyondthebasicstuffwithpython.pdf",
  "think-python": "https://greenteapress.com/thinkpython2/thinkpython2.pdf",
  "python-for-everybody": "https://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf",
  "a-byte-of-python": "https://homepages.uc.edu/~becktl/byte_of_python.pdf",
  "the-hitchhikers-guide": "https://www.rasa-ai.com/wp-content/uploads/2022/02/The-Hitchhikers-Guide-To-Python-PDFDrive-.pdf",
}


def download(name: str, url: str, dest: Path) -> None:
    print(f"-> Descargando {name}")
    subprocess.run(["wget", url, f"--output-document={dest}"], check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path("recursos"),
        help="Carpeta de destino (por defecto: ./recursos)",
    )
    args = parser.parse_args()

    dest: Path = args.dest.expanduser().resolve()
    dest.mkdir(parents=True, exist_ok=True)

    for name, url in REPOS.items():
        download(name, url, dest / f"{name}.pdf")

    return 0


if __name__ == "__main__":
    sys.exit(main())
