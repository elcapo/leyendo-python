# Leyendo Python

Ahora que los ordenadores saben programar, leer y entender código se hace mucho más importante. Por eso, este curso explora una forma diferente de estudiar programación basada en empezar por leer y analizar código de proyectos existentes.

## Índice

Cada capítulo se apoya en una de las librerías de referencia como fuente principal de ejemplos; los cruces son intencionados para releer los mismos repos desde ángulos distintos.

1. **Cómo leer código** — recomendaciones sobre cómo acercarse por primera vez a las fuentes de un programa.
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
16. **Arquitectura de aplicaciones** — modelado de dominio, patrón repositorio, casos de uso, unidades de trabajo y orientación a eventos.
17. **Empaquetado y distribución** — versionado, `build` y publicación en PyPI.
18. **Siguientes pasos** — guía para leer proyectos medianos y grandes, con enlaces a las listas de profundización.

## Criterios de selección

Los repositorios que este curso usa como referencias cumplen, como mínimo:

1. Reputación pública por **buenas prácticas** (tipado, testing, documentación, diseño limpio).
2. **Uso amplio** en la industria o en la comunidad open source.
3. **Código libre**, con licencia abierta y desarrollo en público.
4. **Reducido tamaño** para hacer su estudio asequible.

### Referencias

| Projecto | Descripción |
| --- | --- |
| [click](https://github.com/pallets/click) | Construcción declarativa de CLIs con decoradores. |
| [more-itertools](https://github.com/more-itertools/more-itertools) | Recetas de iteración; lectura muy didáctica sobre generadores. |
| [pendulum](https://github.com/sdispater/pendulum) | Fechas y zonas horarias, con API muy cuidada. |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Cargar variables de entorno desde `.env`. |
| [rich](https://github.com/Textualize/rich) | Renderizado de texto enriquecido en terminal; excelente diseño orientado a objetos. |
| [tenacity](https://github.com/jd/tenacity) | Reintentos con decoradores. |

Para seguir profundizando, una vez terminado el curso, hemos creado algunas listas adicionales:

- [Librerías para profundizar](./docs/referencias-adicionales/librerias-para-profundizar.md)
- [Aplicaciones con interfaces gráficas](./docs/referencias-adicionales/aplicaciones-con-interfaces-graficas.md)
- [Libros de referencia](./docs/referencias-adicionales/libros-de-referencia.md)

## Licencia

Este curso es material libre y se distribuye bajo una [licencia CC0 de Creative Commons](https://creativecommons.org/public-domain/cc0/). Los proyectos enlazados mantienen cada uno su propia licencia.
