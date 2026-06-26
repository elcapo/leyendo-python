# Capítulo 1 — **Cómo leer código**

## Cómo aproximarse a un repositorio

Hoy en día el código fuente de cualquier programa que se precie vive en repositorios con control de versiones. Un repositorio es una carpeta que puede contener archivos y más carpetas dentro. Y el control de versiones permite llevar control de los cambios por los que pasa cada fichero.

El sistema de control de cambios más popular hoy en día es, sin duda, **Git**. Y lo mejor que puedes hacer para familiarizarte rápido con él, si aún no lo conocías, es abrir un repositorio (como [click](https://github.com/pallets/click/)) y explorarlo. Verás que se parece mucho a un explorador de archivos.

### Saber de qué va el proyecto

En el caso de repositorios de programación, en una primera lectura rápida tus ojos deberían de empezar por buscar un archivo **README.md**. En condiciones normales, ahí encontrarás un resumen explicando en qué consiste el proyecto y algunas instrucciones sobre cómo instalarlo y cómo ponerlo en marcha.

> Click es un paquete de Python para crear interfaces de línea de comandos atractivas de forma modular, con el mínimo código necesario. Es el "Kit de Creación de Interfaces de Línea de Comandos". Es altamente configurable, pero incluye configuraciones predeterminadas prácticas.
>
> Fuente: [click/README.md](https://github.com/pallets/click/blob/main/README.md).

### Saber cómo está organizado

* **Estructura de carpetas** — el paquete principal suele estar en `src/<paquete>/` o `<paquete>/`.
* **pyproject.toml** — dependencias, versión mínima de Python y herramientas configuradas.
* **Puntos de entrada** — el `__init__.py` del paquete principal y su `__all__` (si existe) describen la API pública.
* **Tests** — `tests/` es la documentación viva más fiable: muestran casos de uso y contratos.
* **Documentación** — la carpeta `docs/` o la correspondiente web oficial.

Cada capítulo del curso propondrá una ruta de lectura concreta dentro de uno o varios proyectos. Pero antes, es recomendable que prepares tu equipo para explorarlos.

## Preparar el entorno

### Control de versiones con `git`

Con independencia de cuáles son los lenguajes de programación con los que trabajas, se hace imprescindible una herramienta de control de versiones. Y **git** es con diferencia la más usada.

Gracias a **git** puedes pasar de trabajar en una carpeta con ciertos ficheros en un estado determinado, a trabajar en un repositorio, que es una carpeta con histórico de cambios.

Estos cambios permiten mantener ramas con distintas versiones de los contenidos, volver a versiones anteriores de cualquiera de los ficheros, o saber quién y cuándo se hizo cada cambio.

#### Herramientas de consulta online

Cuando un repositorio mantenido con **git** se convierte en un proyecto compartido, es normal querer compartirlo con otra gente para editarlo de forma colaborativa. Para resolver esto, existen dos herramientas básicas:

* [GitHub](https://github.com): El sitio web de repositorios de código más grande del mundo, mantenido por los autores mismos de **git**.

* [GitLab](https://about.gitlab.com): Una alternativa a GitHub que puede ser alojada en servidores privados, o hasta en ordenadores personales.

En la práctica, puedes seguir este curso completo usando únicamente un navegador pero la experiencia no es la misma que la de clonar los repositorios en tu propio ordenador.

Además de que, al clonarlos, ganas la posibilidad de trabajar cuando no tengas conexión a internet y se facilitan enormemente las tareas de lectura, edición y ejecución paso a paso.

Por eso, te recomiendo que sigas las [instrucciones oficiales de instalación de **git**](https://git-scm.com/downloads).

### Gestión de paquetes con `uv`

Aunque entraremos en más detalle sobre las herramientas que debes de conocer para trabajar en proyectos escritos en Python, por el momento es suficiente con que instales **uv**, que es la herramienta que usaremos para gestionar dependencias, incluída la versión específica de Python que necesita cada proyecto.

En la mayor parte de los casos, para instalar **uv** en Linux, o MacOS, o WSL, basta con ejecutar:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Si tienes problemas, sigue las [instrucciones oficiales para instalar uv](https://docs.astral.sh/uv/getting-started/installation/).

### Python

**Python** es el lenguaje de programación sobre el que gira todo el curso. A lo largo de los capítulos vamos a asumir **Python 3.12** o superior, que es la versión con la que funcionan los proyectos de referencia.

Aunque tu sistema operativo ya traiga una versión de Python instalada, es buena práctica dejar que sea **uv** quien gestione una propia, aislada del sistema, ejecutando:

```bash
uv python install 3.12
```

Así el intérprete que usemos en el curso no interfiere ni con el Python del sistema ni con el de otros proyectos que tengas en el ordenador.

### Clonar los repositorios de referencia

**Clonar** un repositorio consiste en descargar una copia local completa —código, historial de cambios y ramas— a una carpeta de tu ordenador. Para evitarte lanzar cada clonación a mano, el curso trae un pequeño script que lo hace por ti.

Desde la raíz del curso:

```bash
uv run scripts/clone_repos.py
```

El script crea la carpeta `repositorios/` y dentro clona los seis proyectos que vamos a estudiar:

| Proyecto | Carpeta local | Origen |
| --- | --- | --- |
| click | `repositorios/click/` | <https://github.com/pallets/click> |
| more-itertools | `repositorios/more-itertools/` | <https://github.com/more-itertools/more-itertools> |
| pendulum | `repositorios/pendulum/` | <https://github.com/sdispater/pendulum> |
| python-dotenv | `repositorios/python-dotenv/` | <https://github.com/theskumar/python-dotenv> |
| rich | `repositorios/rich/` | <https://github.com/Textualize/rich> |
| tenacity | `repositorios/tenacity/` | <https://github.com/jd/tenacity> |

Si más adelante vuelves a ejecutar el script sobre un repositorio ya clonado, en lugar de clonarlo otra vez lo actualiza con los últimos cambios mediante:

```bash
git pull --ff-only
```

El flag `--ff-only` asegura que la actualización solo prospera si puede hacerse avanzando la rama local sin mezclar cambios —útil si alguna vez has tocado la copia local por tu cuenta, porque el script no la pisará en silencio.
