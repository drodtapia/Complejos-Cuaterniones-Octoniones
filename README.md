# Clases de Complejos, Cuaterniones y Octoniones en Python

## Descripción del Programa

Este programa implementa clases para manejar números complejos, cuaterniones y octoniones, proporcionando una variedad de funciones para realizar operaciones matemáticas básicas y demostrar propiedades específicas de estos números.

### Clase Complejos

La clase `Complejos` permite representar y manipular números complejos en forma de `a + bi`, donde `a` es la parte real y `b` es la parte imaginaria del número complejo. Esta clase incluye las siguientes funciones:

1. **Suma:** Sobrecarga del operador `+`.
2. **Resta:** Sobrecarga del operador `-`.
3. **Multiplicación:** Sobrecarga del operador `*`.
4. **División:** Sobrecarga del operador `/`.
5. **Conjugación:** La función `conjugado()` permite obtener el conjugado de un número complejo.
6. **Módulo:** La función `__pow__()` permite calcular el módulo (o la magnitud) de un número complejo.

### Clase Cuaterniones

La clase es la de los `Cuaterniones` es una generalización de los complejos y se forman a partir de dos números complejos que generan las cuatro componentes. Esta clase proporciona funciones similares a las de la clase `Complejos`, adaptadas para trabajar con cuaterniones.

Además, se incluye la demostración de la no conmutatividad de los cuaterniones.

### Clase Octoniones

La clase `Octoniones` permite representar y manipular octoniones, que son extensiones de los cuaterniones en un espacio de ocho dimensiones. Esta clase incluye algunas operaciones simples.

### Ejemplos de Uso

Para probar las clases anteriores, se proporcionan tres archivos de script:

1. **Ejemplo1_.py:** Importa y utiliza la clase `Complejos` para trabajar con tres números complejos introducidos por el usuario. Demuestra cada uno de los métodos definidos para la clase `Complejos`.

2. **Ejemplo_2.py:** Similar a Ejemplo1.py, pero importa la clase `Cuaterniones` y demuestra las funciones definidas para esta clase, además de demostrar la no conmutatividad de los cuaterniones.

3. **Ejemplo_3.py:** Importa y utiliza la clase `Octoniones` para probar los métodos definidos en `octoniones.py`, permitiendo al usuario definir las variables de cada clase de manera interactiva.

Estos scripts permiten al usuario introducir diferentes valores y obtener resultados rápidos y precisos para cada función definida en las clases correspondientes.

### Demostración:
Al ejecutar cualquiera de los scripts de ejemplo y seguir las instrucciones proporcionadas en pantalla, se mostrarán cada uno de los métodos definidos para las clases correspondientes. Cada script de ejemplo permite al usuario ingresar los números necesarios y ver los resultados de las operaciones realizadas. A continuación se muestra una demostración del `Ejemplo_1.py`
```bash
$ py Ejemplo_1.py
Introducir real z1: 1
Introducir imaginario z1: 2
Introducir real z2: 3
Introducir imaginario z2: 4
Introducir real z3: 5
Introducir imaginario z3: 6

Primer complejo z1: (1+2i)
Segundo complejo z2: (3+4i)
Tercer complejo z3: (5+6i)
Suma z1 + z2: (4+6i)
Suma z2 + z3: (8+10i)
Suma z1 + z3: (6+8i)
Suma de z1+z2+z3: (9+12i)
Resta de z1 - z2: (-2-2i)
Resta de z2 - z3: (-2-2i)
Resta de z1 - z3: (-4-4i)
Resta de z1-z2-z3: (-7-8i)
Multiplicacion de z1*z2 (-5+10i)
Multiplicacion de z2*z3 (-9+38i)
Multiplicacion de z1*z3 (-7+16i)
Multiplicacion de z1*z2*z3 (-85+20i)
Division de z1/z2 (0+0i)
Division de z2/z3 (0+0i)
Division de z1/z3 (0+0i)
Division de (z1/z2)/z3
conjugado z1: (1-2i)
conjugado z2: (3-4i)
conjugado z3: (5-6i)
Modulo de z1: 2.23606797749979
Modulo de z2: 5.0
Modulo de z3: 7.810249675906654
```
### Contribución y Colaboración

¡Tu contribución es bienvenida! Si deseas contribuir con mejoras, correcciones o nuevas características, aquí hay algunas formas de hacerlo:

1. **Informar Problemas:** Si encuentras errores o tienes ideas para nuevas características, por favor abre un problema en el [rastreador de problemas](https://github.com/drodtapia/Complejos-Cuaterniones-Octoniones/issues).
   
2. **Enviar Pull Requests:** Si has realizado mejoras en el código, puedes enviar un pull request. Asegúrate de que tu código esté bien probado y documentado.

3. **Comentar y Discutir:** Incluso si no puedes contribuir con código, puedes participar en las discusiones sobre problemas y características. Tus comentarios son valiosos para mejorar el proyecto.

4. **Compartir:** ¡Ayuda a difundir este proyecto compartiéndolo con tus amigos y colegas!

¡Gracias por tu interés en contribuir al proyecto!

### Licencia

Este proyecto está bajo la Licencia [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

Esto significa que puedes:

- Compartir: copiar y redistribuir el material en cualquier medio o formato.
- Adaptar: remezclar, transformar y construir sobre el material.

Bajo los siguientes términos:

- Atribución: debes dar crédito de manera adecuada, proporcionar un enlace a la licencia e indicar si se han realizado cambios. Puedes hacerlo de cualquier manera razonable, pero no de una manera que sugiera que el licenciante te respalda a ti o al uso que haces del material.
- No Comercial: no puedes utilizar el material con fines comerciales.

Leer el texto completo de la licencia [aquí](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

### Créditos y Reconocimientos
Desarrollado por David Rodríguez.

### Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactar a drodtapia@gmail.com.
