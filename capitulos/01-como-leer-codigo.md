# Capítulo 1 — **Cómo leer código**

## Cómo aproximarse a un repositorio

Hoy en día el código fuente de cualquier programa que se precie vive en repositorios con control de versiones. Un repositorio es una carpeta que puede contener archivos y más carpetas dentro. Y el control de versiones es un sistema que permite llevar control de los cambios por los que pasa cada fichero.

El sistema de control de cambios más popular hoy en día es, sin duda, **Git**. Y lo mejor que puedes hacer para familiarizarte rápido con él, si aún no lo conocías, es abrir un repositorio (como [click](https://github.com/pallets/click/)) y explorarlo. Verás que se parece mucho a un explorador de archivos.

### Saber cómo está organizado

Ya sabes de qué va el proyecto; ahora toca orientarte dentro de él. Un repositorio
Python moderno suele seguir un esquema parecido a este, tomado de
[click](https://github.com/pallets/click):

```
click/
├── README.md              # presentación e instrucciones básicas
├── LICENSE.txt            # condiciones de uso, reproducción y copia
├── pyproject.toml         # metadatos, dependencias y herramientas
├── src/click/             # carpeta con el código fuente del paquete
│   ├── __init__.py        # métodos expuestos
│   ├── core.py            # módulos del paquete
│   └── _utils.py          # archivos internos identificados con un guion bajo
├── tests/                 # casos de uso y contratos
├── examples/              # pequeñas recetas de código listas para ejecutar
└── docs/                  # documentación generada
```

#### El archivo `README.md`

Cuando veas por primera vez el código fuente de un programa que no conocías previamente, en una primera lectura rápida tus ojos deberían de empezar por buscar un archivo **README.md**. En condiciones normales, ahí encontrarás un resumen explicando en qué consiste el proyecto y algunas instrucciones sobre cómo instalarlo y cómo ponerlo en marcha.


> **Ejemplo**
>
> Click es un paquete de Python para crear interfaces de línea de comandos atractivas de forma modular, con el mínimo código necesario. Es el "Kit de Creación de Interfaces de Línea de Comandos". Es altamente configurable, pero incluye configuraciones predeterminadas prácticas.
>
> Archivo completo: [click/README.md](https://github.com/pallets/click/blob/main/README.md).


#### Código fuente

El código fuente es el conjunto de archivos con código Python. Lo normal es que consista en archivos con extensión **.py**. Dentro de ese conjunto de archivos podemos distinguir tres tipos según el nombre que tengan.

En primer lugar están los módulos, que son los archivos cuyo nombre empieza por una letra (ej. [core.py](https://github.com/pallets/click/blob/main/src/click/core.py)). Estos son los archivos "normales": contienen código que escribes para que tu programa haga su trabajo y puedes importarlos o ejecutarlos directamente cuando lo necesites.

Junto a ellos existen otros dos tipos que se reconocen por empezar con guiones bajos. Los que comienzan con un guión bajo (ej. [_utils.py](https://github.com/pallets/click/blob/main/src/click/_utils.py)) son archivos "internos": su autor indica con ese prefijo que están pensados para usarse dentro del paquete y no forman parte de la interfaz pública que se espera que uses desde fuera.

Por último, los archivos que empiezan con dos guiones bajos (ej. [__init__.py](https://github.com/pallets/click/blob/main/src/click/__init__.py)) tienen un significado especial para el propio Python y el lenguaje los reserva para funciones concretas, por ejemplo para marcar que una carpeta es un paquete o para definir comportamientos de inicialización.

La ubicación del código fuente varía. Lo más habitual es encontrarlo en **src/\<paquete\>/** aunque en muchos proyectos está directamente en **\<paquete\>/** (ej. [rich](https://github.com/Textualize/rich)). También es habitual encontrar repositorios más maduros que siguen convenciones que ya no se usan tanto, como **lib/\<paquete\>/** pero que antaño fueron estándar (ej. [ansible](https://github.com/ansible/ansible)).
