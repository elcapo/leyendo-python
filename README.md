# Leyendo Python

Curso de Python basado en la **lectura de código fuente** de proyectos reales y reconocidos por aplicar buenas prácticas.

## Filosofía

Ahora que los ordenadores saben programar, leer y entender código se hace gana peso frente a escribirlo desde cero. Por eso, este curso explora una forma diferente de estudiar programación basada en empezar por leer y analizar código de proyectos existentes.

Igual que aprendemos a entender el lenguaje antes de aprender a hablarlo, antes de construir nuestras propias abstracciones, conviene entender cómo las construyen en proyectos sólidos y bien estructurados.

## Índice (borrador)

Cada capítulo se apoya en una de las librerías de referencia como fuente principal de ejemplos; los cruces son intencionados para releer los mismos repos desde ángulos distintos.

1. **Cómo leer código** — metodología del curso, setup (Python, `uv`) y clonado de los repos de referencia.
2. **Sintaxis y tipos básicos** — variables, primitivas, operadores, condicionales y bucles.
3. **Colecciones e iteración** — listas, tuplas, diccionarios, conjuntos, comprehensions, iteradores y generadores.
4. **Funciones** — argumentos, `*args`/`**kwargs`, closures, lambdas y decoradores.
5. **Manejo de errores** — `try`/`except`/`finally`, jerarquía de excepciones y excepciones propias.
6. **Clases e introducción a la orientación a objetos** — atributos, métodos, *dunders*, herencia vs composición y `dataclass`.
7. **Tipado estático** — `typing`, `Protocol`, `TypeVar`, `Optional` y `TYPE_CHECKING`.
8. **Context managers y gestión de recursos** — `with`, `contextlib`, ficheros y `pathlib`.
9. **Programación asíncrona** — `async`/`await`, corrutinas, `asyncio`, iteradores y context managers asíncronos.
10. **Módulos y paquetes** — `import`, `__init__.py`, imports relativos, `__all__` y separación entre API pública e interna.
11. **Tests con pytest** — fixtures, parametrización, *mocks* y cobertura.
12. **Tooling moderno** — entorno virtual con `uv`, `pyproject.toml`, `ruff`, `mypy`, `pre-commit` y CI en GitHub Actions.
13. **Documentación** — docstrings (estilo Google/NumPy), Sphinx/MkDocs y ejemplos ejecutables.
14. **Logging** — el módulo `logging` de la librería estándar, *loggers*, *handlers*, niveles, configuración y buenas prácticas.
15. **Patrones de desarrollo** — inmutabilidad y APIs fluidas, decoradores como puntos de extensión, composición sobre herencia, funciones puras y *pipelines* de iteración.
16. **Empaquetado y distribución** — versionado, `build` y publicación en PyPI.
17. **Siguientes pasos** — guía para leer proyectos medianos y grandes, con enlaces a las listas de profundización.

## Criterios de selección

Los repositorios que este curso usa como referencias cumplen, como mínimo:

1. Reputación pública por **buenas prácticas** (tipado, testing, documentación, diseño limpio).
2. **Uso amplio** en la industria o en la comunidad open source.
3. **Código libre**, con licencia abierta y desarrollo en público.
4. **Reducido tamaño** para hacer su estudio asequible.

### Referencias

| Proyecto | Enlaces | Último commit | Tamaño | Descripción |
| --- | --- | ---: | ---: | --- |
| click | [GitHub](https://github.com/pallets/click)<br/>[Docs](https://click.palletsprojects.com/) | 2026-04-03 | 22.615 líneas<br/>1,3 MB | Construcción declarativa de CLIs con decoradores. |
| more-itertools | [GitHub](https://github.com/more-itertools/more-itertools)<br/>[Docs](https://more-itertools.readthedocs.io/) | 2026-04-22 | 15.916 líneas<br/>639,1 KB | Recetas de iteración; lectura muy didáctica sobre generadores. |
| pendulum | [GitHub](https://github.com/sdispater/pendulum)<br/>[Docs](https://pendulum.eustace.io/docs/) | 2026-03-30 | 25.518 líneas<br/>1.002,6 KB |Fechas y zonas horarias, con API muy cuidada. |
| python-dotenv | [GitHub](https://github.com/theskumar/python-dotenv)<br/>[Docs](https://saurabh-kumar.com/python-dotenv/) | 2026-04-20 | 3.230 líneas<br/>157,4 KB | Cargar variables de entorno desde `.env`. |
| rich | [GitHub](https://github.com/Textualize/rich)<br/>[Docs](https://rich.readthedocs.io/) | 2026-04-12 | 51.866 líneas<br/>18,8 MB | Renderizado de texto enriquecido en terminal; excelente diseño orientado a objetos. |
| tenacity | [GitHub](https://github.com/jd/tenacity)<br/>[Docs](https://tenacity.readthedocs.io/) | 2026-03-23 | 5.267 líneas<br/>242,6 KB | Reintentos con decoradores. |

Para seguir profundizando, una vez terminado el curso, hemos creado algunas listas adicionales:

- [Librerías de tamaño mediano y grande](./docs/referencias-adicionales/librerias-para-profundizar.md)
- [Aplicaciones con interfaces gráficas](./docs/referencias-adicionales/aplicaciones-con-interfaces-graficas.md)

## Licencia

Este curso es material libre y se distribuye bajo una [licencia CC0 de Creative Commons](https://creativecommons.org/public-domain/cc0/). Los proyectos enlazados mantienen cada uno su propia licencia.
