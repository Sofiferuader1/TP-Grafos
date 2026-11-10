# Trabajo Práctico – Grafos

**Materia:** Algoritmos y Estructuras de Datos  
**Tema:** Grafos  
**Ejercicios:** 5 y 14

## Descripción

Este trabajo práctico consiste en resolver los ejercicios 5 y 14 de la guía de grafos del libro *Algoritmos y estructuras de datos en Python*.

Los ejercicios fueron desarrollados en Python utilizando grafos no dirigidos y algoritmos de recorridos, caminos mínimos y árboles de expansión mínima.

## Ejercicio 5 – Red informática

Se representa una red informática mediante un grafo no dirigido, donde los vértices corresponden a equipos y las aristas representan sus conexiones.

Se resuelven las siguientes actividades:

- Almacenar el nombre y tipo de cada equipo.
- Realizar recorridos en profundidad (DFS) y amplitud (BFS) desde las notebooks Red Hat, Debian y Arch.
- Encontrar los caminos más cortos desde Manjaro, Red Hat y Fedora hasta la impresora.
- Obtener el árbol de expansión mínima.
- Determinar qué PC tiene el camino más corto hasta el servidor Guaraní.
- Identificar la computadora del Switch 1 más cercana al servidor MongoDB.
- Cambiar la conexión de la impresora al Router 2 y repetir los recorridos.

**Archivo:** `ejercicio_5.py`

## Ejercicio 14 – Ambientes de una casa

Se representa una casa mediante un grafo no dirigido, donde cada vértice corresponde a un ambiente y las aristas representan conexiones con distancias expresadas en metros.

Se resuelven las siguientes actividades:

- Crear los 11 ambientes de la casa.
- Establecer al menos tres conexiones por ambiente y cinco conexiones en dos de ellos.
- Obtener el árbol de expansión mínima para calcular la cantidad de cable necesario.
- Determinar el camino más corto desde la habitación 1 hasta la sala de estar.

Las distancias utilizadas son valores de ejemplo definidos para el ejercicio.

**Resultados obtenidos:**

- Árbol de expansión mínima: **58 metros de cable**.
- Camino más corto: Habitación 1 → Habitación 2 → Sala de estar.
- Cable necesario para ese recorrido: **10 metros**.

**Archivo:** `ejercicio_14.py`

## Tecnologías y algoritmos utilizados

- Python 3
- Grafos no dirigidos
- Recorridos DFS y BFS
- Algoritmo de Dijkstra
- Árboles de expansión mínima

## Ejecución

Para ejecutar los programas, abrir una terminal en la carpeta del proyecto y utilizar los siguientes comandos:

**Ejercicio 5:**

```bash
python ejercicio_5.py
```

**Ejercicio 14:**

```bash
python ejercicio_14.py
```

Los resultados se muestran directamente en la terminal.