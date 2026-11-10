from collections import deque
import heapq

# Grafo no dirigido: cada conexion tiene un peso.
grafo = {}
tipos = {}


def agregar_equipo(nombre, tipo):
    grafo[nombre] = {}
    tipos[nombre] = tipo


def conectar(a, b, peso):
    grafo[a][b] = peso
    grafo[b][a] = peso


def desconectar(a, b):
    del grafo[a][b]
    del grafo[b][a]


def profundidad(inicio):
    visitados = set()
    recorrido = []

    def visitar(actual):
        visitados.add(actual)
        recorrido.append(actual)
        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitar(vecino)

    visitar(inicio)
    return recorrido


def amplitud(inicio):
    visitados = {inicio}
    cola = deque([inicio])
    recorrido = []
    while cola:
        actual = cola.popleft()
        recorrido.append(actual)
        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    return recorrido


def camino_mas_corto(inicio, destino):
    # Dijkstra encuentra el camino de menor peso acumulado.
    cola = [(0, inicio, [inicio])]
    distancias = {inicio: 0}
    while cola:
        distancia, actual, camino = heapq.heappop(cola)
        if distancia > distancias[actual]:
            continue
        if actual == destino:
            return distancia, camino
        for vecino, peso in grafo[actual].items():
            nueva = distancia + peso
            if nueva < distancias.get(vecino, float('inf')):
                distancias[vecino] = nueva
                heapq.heappush(cola, (nueva, vecino, camino + [vecino]))
    return float('inf'), []


def arbol_expansion_minima():
    # Prim conecta todos los equipos con el menor peso total.
    inicio = next(iter(grafo))
    visitados = {inicio}
    aristas = []
    cola = [(peso, inicio, vecino) for vecino, peso in grafo[inicio].items()]
    heapq.heapify(cola)
    total = 0
    while cola and len(visitados) < len(grafo):
        peso, origen, destino = heapq.heappop(cola)
        if destino in visitados:
            continue
        visitados.add(destino)
        aristas.append((origen, destino, peso))
        total += peso
        for vecino, peso_vecino in grafo[destino].items():
            if vecino not in visitados:
                heapq.heappush(cola, (peso_vecino, destino, vecino))
    return aristas, total


# a) Cargar los equipos con su nombre y tipo.
for nombre in ['Ubuntu', 'Mint', 'Manjaro', 'Fedora', 'Parrot']:
    agregar_equipo(nombre, 'pc')
for nombre in ['Red Hat', 'Debian', 'Arch']:
    agregar_equipo(nombre, 'notebook')
for nombre in ['Guaraní', 'MongoDB']:
    agregar_equipo(nombre, 'servidor')
for numero in range(1, 4):
    agregar_equipo(f'Router {numero}', 'router')
for numero in range(1, 3):
    agregar_equipo(f'Switch {numero}', 'switch')
agregar_equipo('Impresora', 'impresora')

# Conexiones y pesos copiados del esquema del libro.
conexiones = [
    ('Debian', 'Switch 1', 17),
    ('Ubuntu', 'Switch 1', 18),
    ('Impresora', 'Switch 1', 22),
    ('Mint', 'Switch 1', 80),
    ('Switch 1', 'Router 1', 29),
    ('Router 1', 'Router 2', 37),
    ('Router 1', 'Router 3', 43),
    ('Router 2', 'Router 3', 50),
    ('Red Hat', 'Router 2', 25),
    ('Guaraní', 'Router 2', 9),
    ('Router 3', 'Switch 2', 61),
    ('Switch 2', 'Manjaro', 40),
    ('Switch 2', 'Parrot', 12),
    ('Switch 2', 'Fedora', 3),
    ('Switch 2', 'MongoDB', 5),
    ('Switch 2', 'Arch', 56),
]
for origen, destino, peso in conexiones:
    conectar(origen, destino, peso)

# b) Recorridos desde las tres notebooks.
print('b) Recorridos en profundidad y amplitud')
for notebook in ['Red Hat', 'Debian', 'Arch']:
    print(f'{notebook}:')
    print('  Profundidad:', ' -> '.join(profundidad(notebook)))
    print('  Amplitud:  ', ' -> '.join(amplitud(notebook)))

# c) Caminos mas cortos desde las tres PC a la impresora.
print('\nc) Caminos mas cortos a la impresora')
for pc in ['Manjaro', 'Red Hat', 'Fedora']:
    distancia, camino = camino_mas_corto(pc, 'Impresora')
    print(f'{pc}: {" -> ".join(camino)} (peso total: {distancia})')

# d) Arbol de expansion minima.
print('\nd) Arbol de expansion minima')
aristas, total = arbol_expansion_minima()
for origen, destino, peso in aristas:
    print(f'{origen} - {destino}: {peso}')
print('Peso total:', total)

# e) Encontrar la PC (no notebook) mas cercana a Guarani.
print('\ne) PC mas cercana a Guaraní')
pc = [nombre for nombre, tipo in tipos.items() if tipo == 'pc']
mejor_pc = min(pc, key=lambda nombre: camino_mas_corto(nombre, 'Guaraní')[0])
distancia, camino = camino_mas_corto(mejor_pc, 'Guaraní')
print(' -> '.join(camino), '| peso:', distancia)

# f) Computadora conectada al Switch 1 mas cercana a MongoDB.
print('\nf) Computadora del Switch 1 mas cercana a MongoDB')
computadoras = [nombre for nombre in grafo['Switch 1'] if tipos[nombre] in ('pc', 'notebook')]
mejor_equipo = min(computadoras, key=lambda nombre: camino_mas_corto(nombre, 'MongoDB')[0])
distancia, camino = camino_mas_corto(mejor_equipo, 'MongoDB')
print(' -> '.join(camino), '| peso:', distancia)

# g) Mover la impresora del Switch 1 al Router 2 y repetir b).
# Como el enunciado no indica el nuevo peso, se conserva el valor 22.
print('\ng) Impresora conectada al Router 2: nuevos recorridos')
desconectar('Impresora', 'Switch 1')
conectar('Impresora', 'Router 2', 22)
for notebook in ['Red Hat', 'Debian', 'Arch']:
    print(f'{notebook}:')
    print('  Profundidad:', ' -> '.join(profundidad(notebook)))
    print('  Amplitud:  ', ' -> '.join(amplitud(notebook)))

# h) El grafo es no dirigido: cada arista se guarda en ambos sentidos.
