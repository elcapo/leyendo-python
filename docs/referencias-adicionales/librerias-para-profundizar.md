# Leyendo Python

## Librerías medianas (framework o herramienta con arquitectura reconocible)

Ya hay capas, módulos internos y decisiones de diseño que merece la pena discutir.

| Proyecto | GitHub | Documentación | Descripción |
| --- | --- | --- | --- |
| Black | [GitHub](https://github.com/psf/black) | [Docs](https://black.readthedocs.io/) | Formateador; ejemplo excelente de herramienta que analiza AST. |
| FastAPI | [GitHub](https://github.com/fastapi/fastapi) | [Docs](https://fastapi.tiangolo.com/) | API moderna basada en tipos, Pydantic y Starlette. |
| Flask | [GitHub](https://github.com/pallets/flask) | [Docs](https://flask.palletsprojects.com/) | Microframework web; un clásico para entender WSGI y diseño minimalista. |
| httpx | [GitHub](https://github.com/encode/httpx) | [Docs](https://www.python-httpx.org/) | Sucesor moderno de requests con soporte async. |
| Poetry | [GitHub](https://github.com/python-poetry/poetry) | [Docs](https://python-poetry.org/docs/) | Gestor de dependencias y empaquetado. |
| Pydantic | [GitHub](https://github.com/pydantic/pydantic) | [Docs](https://docs.pydantic.dev/) | Validación y parsing basados en tipos; uso intensivo de metaprogramación. |
| pytest | [GitHub](https://github.com/pytest-dev/pytest) | [Docs](https://docs.pytest.org/) | Framework de tests; diseño extremadamente extensible vía fixtures y plugins. |
| Requests | [GitHub](https://github.com/psf/requests) | [Docs](https://requests.readthedocs.io/) | La API que definió cómo deberían ser las librerías HTTP. |
| Ruff | [GitHub](https://github.com/astral-sh/ruff) | [Docs](https://docs.astral.sh/ruff/) | Linter/formatter escrito en Rust, pero con integración Python muy pulida. |
| SQLModel | [GitHub](https://github.com/fastapi/sqlmodel) | [Docs](https://sqlmodel.tiangolo.com/) | Integración Pydantic + SQLAlchemy. |
| Starlette | [GitHub](https://github.com/encode/starlette) | [Docs](https://www.starlette.dev/) | Toolkit ASGI sobre el que se construye FastAPI. |
| Textual | [GitHub](https://github.com/Textualize/textual) | [Docs](https://textual.textualize.io/) | TUI moderno construido sobre Rich. |
| Typer | [GitHub](https://github.com/fastapi/typer) | [Docs](https://typer.tiangolo.com/) | CLIs tipadas encima de click. |

## Librerías grandes (ecosistemas completos)

Lectura selectiva: no se leen enteros, se exploran módulos y se estudian decisiones arquitectónicas.

| Proyecto | GitHub | Documentación | Descripción |
| --- | --- | --- | --- |
| Ansible | [GitHub](https://github.com/ansible/ansible) | [Docs](https://docs.ansible.com/) | Automatización declarativa; interesante por su arquitectura de plugins. |
| CPython | [GitHub](https://github.com/python/cpython) | [Docs](https://docs.python.org/3/) | El intérprete de referencia. Leer su `Lib/` enseña Python idiomático escrito por el core team. |
| Celery | [GitHub](https://github.com/celery/celery) | [Docs](https://docs.celeryq.dev/) | Colas de tareas distribuidas. |
| Django | [GitHub](https://github.com/django/django) | [Docs](https://docs.djangoproject.com/) | Framework web maduro, con convenciones muy consolidadas. |
| mypy | [GitHub](https://github.com/python/mypy) | [Docs](https://mypy.readthedocs.io/) | Chequeo estático de tipos; un proyecto escrito en Python que analiza Python. |
| SQLAlchemy | [GitHub](https://github.com/sqlalchemy/sqlalchemy) | [Docs](https://docs.sqlalchemy.org/) | ORM y toolkit SQL; referente en diseño orientado a expresiones. |
| NumPy | [GitHub](https://github.com/numpy/numpy) | [Docs](https://numpy.org/doc/) | Fundamentos del cómputo numérico en Python. |
| pandas | [GitHub](https://github.com/pandas-dev/pandas) | [Docs](https://pandas.pydata.org/docs/) | Análisis de datos; ejemplo de librería con API compleja y alto rendimiento. |
| scikit-learn | [GitHub](https://github.com/scikit-learn/scikit-learn) | [Docs](https://scikit-learn.org/stable/) | Machine learning clásico; consistencia de API ejemplar. |
| Scrapy | [GitHub](https://github.com/scrapy/scrapy) | [Docs](https://docs.scrapy.org/) | Framework de crawling y scraping; arquitectura con engine, spiders, middlewares y pipelines. |
