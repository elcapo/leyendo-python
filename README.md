# Leyendo Python

Ahora que los ordenadores saben programar, leer y entender código se hace más importante que nunca. Por eso, este curso explora una forma diferente de estudiar programación basada en leer y analizar código de proyectos existentes.

## Índice

1. **Cómo leer código** — recomendaciones para acercarte por primera vez al código fuente de un programa sin agobios.
2. **Sintaxis y tipos básicos** — variables, datos elementales, operadores, condicionales y bucles.
3. **Colecciones e iteración** — listas, tuplas, diccionarios y conjuntos, además de formas compactas de recorrerlos y construirlos.
4. **Funciones** — cómo pasar argumentos flexibles, reutilizar lógica en funciones anidadas, escribir funciones pequeñas y envolver otras para cambiar su comportamiento.
5. **Manejo de errores** — cómo detectar y tratar fallos sin que el programa se detenga, los tipos de excepción que existen y cómo crear las tuyas.
6. **Clases e introducción a la orientación a objetos** — atributos, métodos, métodos especiales, cuándo heredar y cuándo componer, y una forma sencilla de definir clases de datos.
7. **Tipado estático** — cómo añadir pistas de tipo al código, definir interfaces y tipos genéricos, marcar valores opcionales y separar las importaciones de tipo cuando haga falta.
8. **Gestión de recursos** — cómo abrir y cerrar ficheros y otros recursos de forma segura usando bloques contextuales y utilidades de la librería estándar.
9. **Programación asíncrona** — cómo escribir código que espera sin bloquear, con corrutinas y el bucle de eventos, incluida la iteración y la gestión de recursos asíncrona.
10. **Módulos y paquetes** — cómo organizar tu código en varios archivos, exponer solo lo necesario y separar la API pública de los detalles internos.
11. **Tests con pytest** — cómo preparar datos de prueba de forma reutilizable, ejecutar el mismo test con varios casos, simular dependencias y medir la cobertura.
12. **Tooling moderno** — cómo aislar dependencias y mantener el código limpio y consistente, desde el entorno virtual hasta la integración continua.
13. **Documentación** — cómo escribir explicaciones útiles dentro del propio código, generar documentación del proyecto y mantener ejemplos ejecutables.
14. **Logging** — cómo registrar lo que hace tu programa, con distintos niveles de detalle y destinos, y buenas prácticas para no llenar el disco de ruido.
15. **Patrones de desarrollo** — inmutabilidad, interfaces fluidas, composición frente a herencia, funciones puras y encadenado de operaciones de iteración.
16. **Arquitectura de aplicaciones** — cómo modelar el dominio, separar el acceso a datos con el patrón repositorio, organizar casos de uso y orientar el flujo a eventos.
17. **Empaquetado y distribución** — cómo versionar tu proyecto, construir el paquete y publicarlo en el índice oficial de Python.
18. **Siguientes pasos** — guía para leer proyectos de tamaño mediano y grande, con enlaces a las listas de profundización.

## Criterios de selección

Los repositorios que este curso usa como referencias cumplen, como mínimo:

1. Reputación pública por **buenas prácticas** (tipado, testing, documentación, diseño limpio).
2. **Uso amplio** en la industria o en la comunidad open source.
3. **Código libre**, con licencia abierta y desarrollo en público.
4. **Reducido tamaño** para hacer su estudio asequible.

### Bibliografía

| Título | Escrito por | Descripción |
| --- | --- | --- |
| **Python for everybody** | Charles R. Severance | Introducción muy accesible para quien nunca ha programado.<br/>Destaca por su tono cercano y ejemplos sencillos. |
| **Think Python** | Allen Downey | Enseña a razonar como un programador.<br/>Su punto fuerte es el enfoque en pensamiento computacional y resolución de problemas. |
| **Beyond the basic stuff** | Al Sweigart | Puente entre principiante e intermedio.<br/>Sobresale en buenas prácticas de código limpio y depuración. |
| **The Hitchiker's Guide to Python** | Kenneth Reitz<br/>Tanya Schlusser | Guía de buenas prácticas y tooling.<br/>Destaca como referencia rápida del ecosistema Python moderno. |
| **Architecture Patterns with Python** | Harry J.W. Percival<br/>Bob Gregory | Introduce Domain-Driven Design y patrones de arquitectura.<br/>Su fuerte son los ejemplos de testing y arquitectura hexagonal. |
| **A byte of Python** | Swaroop C H | Manual conciso y gratuito.<br/>Brilla como referencia compacta para principiantes y como repaso para programadores. |

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

## Licencia

Este curso es material libre y se distribuye bajo una [licencia CC0 de Creative Commons](https://creativecommons.org/public-domain/cc0/). Los proyectos enlazados mantienen cada uno su propia licencia.
