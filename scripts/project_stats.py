"""Obtiene métricas básicas de un proyecto Python clonado.

Dado el path a un repositorio, imprime:
- fecha del último commit
- número de líneas en archivos .py
- tamaño total del código fuente tras `git clone`, sin contar artefactos
  generados por la instalación de dependencias ni la carpeta `.git`.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Iterator

EXCLUDED_DIRS = frozenset({
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".tox",
    ".nox",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "node_modules",
    "build",
    "dist",
})


def last_commit_date(repo: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), "log", "-1", "--format=%cs"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def iter_source_files(repo: Path) -> Iterator[Path]:
    for path in repo.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in path.relative_to(repo).parts):
            continue
        yield path


def count_python_lines(repo: Path) -> int:
    total = 0
    for path in iter_source_files(repo):
        if path.suffix != ".py":
            continue
        with path.open("rb") as f:
            total += sum(1 for _ in f)
    return total


def source_size_bytes(repo: Path) -> int:
    return sum(path.stat().st_size for path in iter_source_files(repo))


def format_size(num_bytes: int) -> str:
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path, help="Ruta al repositorio clonado")
    args = parser.parse_args()

    repo: Path = args.repo.expanduser().resolve()
    if not repo.is_dir():
        print(f"No es un directorio: {repo}", file=sys.stderr)
        return 1
    if not (repo / ".git").is_dir():
        print(f"No es un repositorio git: {repo}", file=sys.stderr)
        return 1

    print(f"Proyecto:        {repo.name}")
    print(f"Último commit:   {last_commit_date(repo)}")
    print(f"Líneas de .py:   {count_python_lines(repo):,}")
    print(f"Tamaño fuentes:  {format_size(source_size_bytes(repo))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
