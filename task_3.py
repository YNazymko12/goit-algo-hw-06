import heapq

import networkx as nx
import matplotlib.pyplot as plt

# Створення вагового графа
G = nx.Graph()
G.add_edge("Залізнична станція", "Центральний ринок", weight=5)
G.add_edge("Залізнична станція", "Площа Шевченка", weight=7)
G.add_edge("Центральний ринок", "Паркова зона", weight=3)
G.add_edge("Площа Шевченка", "Паркова зона", weight=4)
G.add_edge("Площа Шевченка", "Торговий центр", weight=6)
G.add_edge("Паркова зона", "Торговий центр", weight=5)
G.add_edge("Паркова зона", "Міська рада", weight=2)
G.add_edge("Торговий центр", "Міська рада", weight=4)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]
    while pq:
        print("pq: ", pq)
        print("sp:", shortest_paths)
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths

# Використання алгоритму Дейкстри
shortest_paths = dijkstra(G, "Залізнична станція")
print(shortest_paths)

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()