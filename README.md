# 42_Python_Module_03
42_Python_Module_03

# Data Quest: Dominando las Colecciones de Python 

¡Bienvenido a mi repositorio de Data Quest! Este proyecto es un viaje a través de la **Dimensión Píxel**, diseñado para dominar las estructuras de datos fundamentales en Python (v3.10+) aplicadas a la ingeniería de datos y analítica de videojuegos.

A lo largo de estos ejercicios, he desarrollado el sistema **PixelMetrics 3000**, una plataforma de analítica que procesa desde puntuaciones de jugadores hasta flujos de datos masivos en tiempo real.

## 🛠️ Reglas Generales

- **Lenguaje:** Python 3.10+.
- **Estilo:** Código adherido al estándar de linter flake8.
- **Restricciones:** Uso exclusivo de la librería `sys` para argumentos de línea de comandos. No se permite la lectura/escritura de archivos externos.
- **Robustez:** Gestión exhaustiva de excepciones (`try/except`) para evitar caídas del sistema.

## 🕹️ Desglose de los Ejercicios

### [Ex0] Misión de Comandos (ft_command_quest.py)
El nivel inicial se centra en la comunicación entre el usuario y el programa.
- **Objetivo:** Aprender a recibir y procesar datos externos mediante la línea de comandos.
- **Conceptos clave:** Uso de `sys.argv`, conteo de argumentos y visualización limpia de la entrada.

### [Ex1] Procesador de Puntuaciones (ft_score_analytics.py)
Primer contacto con el procesamiento de datos secuenciales.
- **Objetivo:** Construir un motor de clasificación (Score Cruncher) que analice el rendimiento de los jugadores.
- **Estructura:** Listas.
- **Funcionalidad:** Cálculo de promedios, puntuaciones máximas/mínimas y rangos, gestionando errores si se introducen datos no numéricos.

### [Ex2] Rastreador de Posición (ft_coordinate_system.py)
Navegación en mundos 3D.
- **Objetivo:** Implementar un sistema de coordenadas inmutables para puntos de aparición o teletransporte.
- **Estructura:** Tuples.
- **Funcionalidad:** Cálculo de la distancia euclidiana 3D y demostración de la técnica de "desempaquetado" de tuplas.

### [Ex3] Caza de Logros (ft_achievement_tracker.py)
Gestión de trofeos únicos sin duplicados.
- **Objetivo:** Crear un sistema que compare los logros entre diferentes jugadores.
- **Estructura:** Sets (Conjuntos).
- **Funcionalidad:** Uso de operaciones de conjuntos como unión, intersección y diferencia para hallar logros comunes, raros o pendientes.

### [Ex4] Control de Inventario (ft_inventory_system.py)
El corazón de cualquier RPG: la mochila de objetos.
- **Objetivo:** Gestionar inventarios complejos con detalles de cantidad, tipo y valor.
- **Estructura:** Diccionarios.
- **Funcionalidad:** Organización de objetos por categorías, cálculo del valor total del tesoro y procesamiento de transacciones entre jugadores.

### [Ex5] Asistente de Transmisión (ft_data_stream.py)
Magia de eficiencia de memoria para procesar millones de eventos.
- **Objetivo:** Procesar flujos de datos infinitos sin colapsar la memoria del sistema.
- **Estructura:** Generadores (`yield`).
- **Funcionalidad:** Filtrado de eventos en tiempo real y análisis de estadísticas con uso de memoria constante.

### [Ex6] Alquimista de Datos (ft_analytics_dashboard.py)
El jefe final: la transformación elegante de datos.
- **Objetivo:** Crear un panel de control consolidando todas las estructuras anteriores mediante código conciso.
- **Estructura:** Comprensiones (List/Dict/Set comprehensions).
- **Funcionalidad:** Transformar datos en bruto en información valiosa (ej. filtrar máximos goleadores o mapear regiones activas) en una sola línea de código.

## 🚀 Cómo ejecutar

Cada ejercicio se ejecuta desde la terminal pasando los parámetros necesarios:

```bash
# Ejemplo para el procesador de puntuaciones
python3 ex1/ft_score_analytics.py 1500 2300 1800
```
Para generar datos de prueba complejos, puedes utilizar las herramientas proporcionadas en el archivo `data_quest_tools.tar.gz`
