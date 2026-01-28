# Guía del Evaluador: Pixel Data Generator

Usa este Markdown para tener a mano los comandos exactos que "rompen" o validan los ejercicios de tus compañeros.

## Comandos de Generación de Datos

| Ejercicio | Qué genera                       | Comando para evaluar                              |
|-----------|----------------------------------|--------------------------------------------------|
| Ex 0      | Comandos               | `python3 ft_command_quest.py hola 42 mundo "test con espacios"`     |
| Ex 1      | Puntuaciones (Lista)             | `python3 data_generator.py 1 --count 15 --format argv` |
| Ex 2      | Coordenadas 3D (Tuplas)         | `python3 data_generator.py 2 --count 5`         |
| Ex 3      | Logros (Sets/Deduplicación)      | `python3 data_generator.py 3`                    |
| Ex 4      | Inventario (Diccionarios)       | `python3 data_generator.py 4`                    |
| Ex 5      | Eventos (Generadores)           | `python3 data_generator.py 5 --count 50`        |
| Ex 6      | Dashboard (Comprensiones)        | `python3 data_generator.py 6`                    |

## Cómo "Suspender" un ejercicio (Casos de prueba críticos)

Usa estos trucos cuando ejecutes el generador para ver si el código del compañero es robusto:

### Ejercicio 1: Score Analytics
**El truco:** Genera muchos números o ninguno.

**Prueba:**
```bash
python3 ft_score_analytics.py $(python3 data_generator.py 1 --count 0 --format argv)
```
**Resultado esperado:** No debe dar `ZeroDivisionError`. Debe decir "No scores provided".

### Ejercicio 2: Position Tracker
**El truco:** El generador da Tuplas 3D (x, y, z).

**Prueba:** Pásale 3 coordenadas en lugar de 2.

**Resultado esperado:** Si el alumno solo programó para 2D (x, y), su programa podría explotar por un `ValueError` (too many values to unpack). Un buen código debe ignorar la Z o avisar del error.

### Ejercicio 3: Achievement Tracker
**El truco:** El generador crea logros duplicados a propósito.

**Prueba:**
```bash
python3 data_generator.py 3
```
**Resultado esperado:** El programa del alumno DEBE usar un `set()` para limpiar los duplicados. Si en la lista final aparece "first_blood" dos veces, el ejercicio está mal.

## Check-list Pro para el Evaluador
- **¿Es determinista?** El generador usa `seed(42)`. Si tú y el alumno usan la misma semilla, los datos deben ser iguales. Si a él le salen otros números, es que ha tocado el generador (mal).
- **¿Maneja el formato argv?** Fíjate si el alumno sabe pasar los datos del generador a su script usando el símbolo `$` o copiando la línea de texto.
- **¿Limpieza (Flake8)?** Antes de probar los datos, corre:
```bash
flake8 nombre_del_archivo.py
```
Si salen más de 5 errores de formato, desaprobado por falta de limpieza.
