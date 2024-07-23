import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин
nodes = [
    "Залізнична станція",
    "Центральний ринок",
    "Площа Шевченка",
    "Паркова зона",
    "Торговий центр",
    "Міська рада"
]
G.add_nodes_from(nodes)

# Додавання ребер
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

# Візуалізація графа
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_size=700, node_color="lightblue", font_size=14, font_weight="bold", edge_color="gray")
plt.title("Транспортна мережа невеликого міста")
plt.show()

# Аналіз основних характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree = dict(G.degree())
average_degree = round(sum(degree.values()) / num_nodes, 2)

print("Кількість вершин:", num_nodes)
print("Кількість ребер:", num_edges)
print("Ступінь кожної вершини:", degree)
print("Середній ступінь вершин:", average_degree)
