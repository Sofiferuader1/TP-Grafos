import heapq

# EJERCICIO 14 - Guia de grafos
# Representamos los ambientes de una casa con un grafo no dirigido.
# Los pesos son distancias de ejemplo en metros, ya que la consigna
# no proporciona un plano ni distancias especificas.

grafo = {}


def agregar_ambiente(nombre):
    # Cada ambiente es un vertice del grafo.
    grafo[nombre] = {}


def conectar(origen, destino, metros):
    # Al ser no dirigido, guardamos la conexion en ambos sentidos.
    grafo[origen][destino] = metros
    grafo[destino][origen] = metros


def arbol_expansion_minima():
    # Algoritmo de Prim: conecta todos los ambientes con el menor
    # total posible de metros de cable.
    inicio = next(iter(grafo))
    visitados = {inicio}
    pendientes = []
    aristas_arbol = []
    total_metros = 0

    for vecino, metros in grafo[inicio].items():
        heapq.heappush(pendientes, (metros, inicio, vecino))

    while pendientes and len(visitados) < len(grafo):
        metros, origen, destino = heapq.heappop(pendientes)
        if destino in visitados:
            continue

        visitados.add(destino)
        aristas_arbol.append((origen, destino, metros))
        total_metros += metros

        for vecino, distancia in grafo[destino].items():
            if vecino not in visitados:
                heapq.heappush(pendientes, (distancia, destino, vecino))

    return aristas_arbol, total_metros


def camino_mas_corto(inicio, destino):
    # Algoritmo de Dijkstra: busca el camino con menor suma de metros.
    distancias = {ambiente: float('inf') for ambiente in grafo}
    anteriores = {}
    distancias[inicio] = 0
    pendientes = [(0, inicio)]

    while pendientes:
        metros_actuales, actual = heapq.heappop(pendientes)
        if metros_actuales > distancias[actual]:
            continue
        if actual == destino:
            break

        for vecino, metros in grafo[actual].items():
            nueva_distancia = metros_actuales + metros
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = actual
                heapq.heappush(pendientes, (nueva_distancia, vecino))

    if distancias[destino] == float('inf'):
        return [], float('inf')

    # Reconstruimos el camino desde el destino hasta el inicio.
    camino = [destino]
    while camino[-1] != inicio:
        camino.append(anteriores[camino[-1]])
    camino.reverse()
    return camino, distancias[destino]


# a) Crear los 11 ambientes solicitados.
ambientes = [
    'Cocina', 'Comedor', 'Cochera', 'Quincho', 'Baño 1',
    'Baño 2', 'Habitación 1', 'Habitación 2',
    'Sala de estar', 'Terraza', 'Patio'
]
for ambiente in ambientes:
    agregar_ambiente(ambiente)

# b) Conectar los ambientes y cargar las distancias en metros.
# Estas son distancias de ejemplo, que podemos modificar.
# Cada ambiente tiene al menos 3 conexiones; Cocina y Baño 2 tienen 5.
conexiones = [
    ('Cocina', 'Comedor', 4),
    ('Comedor', 'Cochera', 9),
    ('Cochera', 'Quincho', 7),
    ('Quincho', 'Baño 1', 6),
    ('Baño 1', 'Baño 2', 5),
    ('Baño 2', 'Habitación 1', 7),
    ('Habitación 1', 'Habitación 2', 4),
    ('Habitación 2', 'Sala de estar', 6),
    ('Sala de estar', 'Terraza', 8),
    ('Terraza', 'Patio', 5),
    ('Patio', 'Cocina', 6),
    ('Cocina', 'Cochera', 10),
    ('Comedor', 'Quincho', 8),
    ('Cochera', 'Baño 1', 11),
    ('Quincho', 'Baño 2', 9),
    ('Baño 1', 'Habitación 1', 8),
    ('Baño 2', 'Habitación 2', 10),
    ('Habitación 1', 'Sala de estar', 12),
    ('Habitación 2', 'Terraza', 9),
    ('Sala de estar', 'Patio', 10),
    ('Terraza', 'Cocina', 12),
    ('Patio', 'Comedor', 11),
    ('Cocina', 'Baño 2', 14),
]
for origen, destino, metros in conexiones:
    conectar(origen, destino, metros)

# Comprobar que se respeten los requisitos de las conexiones.
assert all(len(vecinos) >= 3 for vecinos in grafo.values())
assert sum(len(vecinos) == 5 for vecinos in grafo.values()) == 2

print('EJERCICIO 14 - GRAFO DE UNA CASA')
print('\na) y b) Ambientes y cantidad de conexiones:')
for ambiente, vecinos in grafo.items():
    print(f'  {ambiente}: {len(vecinos)} conexiones')

# c) Arbol de expansion minima.
aristas, total = arbol_expansion_minima()
print('\nc) Arbol de expansion minima:')
for origen, destino, metros in aristas:
    print(f'  {origen} - {destino}: {metros} metros')
print(f'Total de cable para conectar los ambientes: {total} metros')

# d) Camino minimo desde Habitacion 1 hasta Sala de estar.
camino, metros = camino_mas_corto('Habitación 1', 'Sala de estar')
print('\nd) Camino mas corto desde Habitacion 1 hasta Sala de estar:')
print('  ' + ' -> '.join(camino))
print(f'Cable necesario para conectar el router con el Smart TV: {metros} metros')
