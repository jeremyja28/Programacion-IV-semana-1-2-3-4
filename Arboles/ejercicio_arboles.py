# Importamos la librería matplotlib para generar gráficos (plt es el alias común).
import matplotlib.pyplot as plt

# Importamos la librería networkx para trabajar con grafos dirigidos (nx es el alias común).
import networkx as nx

# Creamos un nuevo grafo dirigido (DiGraph significa "Directed Graph", es decir, con flechas).
G = nx.DiGraph()

# Definimos las conexiones (aristas) entre los nodos. Cada tupla representa una conexión de padre a hijo.
edges = [
    ('*', '+'),  # El nodo raíz '*' tiene como hijo izquierdo el operador '+'
    ('*', '-'),  # El nodo raíz '*' tiene como hijo derecho el operador '-'
    ('+', '3'),  # El nodo '+' tiene como hijo izquierdo el operando '3'
    ('+', '5'),  # El nodo '+' tiene como hijo derecho el operando '5'
    ('-', '2'),  # El nodo '-' tiene como hijo izquierdo el operando '2'
    ('-', '1')   # El nodo '-' tiene como hijo derecho el operando '1'
]

# Agregamos todas las aristas al grafo G. NetworkX creará automáticamente los nodos implicados.
G.add_edges_from(edges)

# Definimos las posiciones en el plano (x, y) para que el árbol se visualice ordenado y jerárquico.
pos = {
    '*': (0, 2),      # La raíz está en el nivel más alto
    '+': (-1, 1),     # Hijo izquierdo de '*'
    '-': (1, 1),      # Hijo derecho de '*'
    '3': (-1.5, 0),   # Hijo izquierdo de '+'
    '5': (-0.5, 0),   # Hijo derecho de '+'
    '2': (0.5, 0),    # Hijo izquierdo de '-'
    '1': (1.5, 0)     # Hijo derecho de '-'
}

# Creamos una nueva figura de tamaño 8x5 pulgadas
plt.figure(figsize=(8, 5))

# Dibujamos el grafo:
# - G: el grafo a dibujar
# - pos: las posiciones definidas para cada nodo
# - with_labels=True: muestra los nombres (etiquetas) de los nodos
# - node_color='lightblue': color de los nodos
# - node_size=2000: tamaño de los nodos
# - font_size=14, font_weight='bold': tamaño y grosor del texto
# - arrows=True: muestra flechas indicando dirección
nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=14,
    font_weight='bold',
    arrows=True
)

# Título del gráfico
plt.title("Árbol de expresión: (3 + 5) * (2 - 1)")

# Muestra el gráfico en pantalla
plt.show()
