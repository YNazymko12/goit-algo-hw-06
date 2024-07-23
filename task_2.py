import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф, як у завданні 1
G = nx.Graph()
nodes = [
    "Залізнична станція",
    "Центральний ринок",
    "Площа Шевченка",
    "Паркова зона",
    "Торговий центр",
    "Міська рада"
]
G.add_nodes_from(nodes)

edges = [
    ("Залізнична станція", "Центральний ринок"),
    ("Залізнична станція", "Площа Шевченка"),
    ("Центральний ринок", "Паркова зона"),
    ("Площа Шевченка", "Паркова зона"),
    ("Площа Шевченка", "Торговий центр"),
    ("Паркова зона", "Торговий центр"),
    ("Паркова зона", "Міська рада"),
    ("Торговий центр", "Міська рада")
]
G.add_edges_from(edges)

# Функція для пошуку шляху за допомогою DFS
def dfs(graph, start, visited=None, path=None, parent=None):
    if visited is None:
        visited = set()
        path = []
    if start in visited:
        return
    visited.add(start)
    print(f"DFS: visited {start}")
    if parent is not None:
        path.append((parent, start))
    for next in graph[start]:
        dfs(graph, next, visited, path, start)
    return path

# Функція для пошуку шляху за допомогою BFS
def bfs(graph, start):
    visited, queue = {start}, [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        print(f"BFS: visited {vertex}")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path.append((vertex, neighbour))
    return path

# Знаходження шляхів за допомогою DFS та BFS
start_node = "Залізнична станція"

dfs_path = dfs(G, start_node)
bfs_path = bfs(G, start_node)

print("\nШлях, знайдений за допомогою DFS:")
print(dfs_path)

print("\nШлях, знайдений за допомогою BFS:")
print(bfs_path)

# Візуалізація графа
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_size=700, node_color="lightblue", font_size=14, font_weight="bold", edge_color="gray")
plt.title("Транспортна мережа невеликого міста")
plt.show()