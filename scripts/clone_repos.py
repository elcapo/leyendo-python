"""Clona los repositorios de referencia del curso en ./repositorios/.

Si la carpeta de un repositorio ya existe, se actualiza con `git pull --ff-only`
en lugar de volver a clonar. No se hace checkout a una versión concreta: los
enlaces dentro del curso apuntan a commits específicos en GitHub para no
depender del estado actual de la rama principal.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPOS: dict[str, str] = {
    "click": "https://github.com/pallets/click.git",
    "more-itertools": "https://github.com/more-itertools/more-itertools.git",
    "pendulum": "https://github.com/sdispater/pendulum.git",
    "python-dotenv": "https://github.com/theskumar/python-dotenv.git",
    "rich": "https://github.com/Textualize/rich.git",
    "tenacity": "https://github.com/jd/tenacity.git",
}


def clone_or_update(name: str, url: str, dest: Path) -> None:
    target = dest / name
    if target.exists():
        print(f"-> Actualizando {name}")
        subprocess.run(
            ["git", "-C", str(target), "pull", "--ff-only"],
            check=True,
        )
    else:
        print(f"-> Clonando {name}")
        subprocess.run(["git", "clone", url, str(target)], check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path("repositorios"),
        help="Carpeta de destino (por defecto: ./repositorios)",
    )
    args = parser.parse_args()

    dest: Path = args.dest.expanduser().resolve()
    dest.mkdir(parents=True, exist_ok=True)

    for name, url in REPOS.items():
        clone_or_update(name, url, dest)

    return 0


if __name__ == "__main__":
    sys.exit(main())
