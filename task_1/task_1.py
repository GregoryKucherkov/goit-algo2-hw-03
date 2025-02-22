import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

from edmonds_karp import edmonds_karp

# We create Graph
G = nx.DiGraph()

# edges is the system itself with capacity
edges = [
    ("Terminal 1", "Depo 1", 25),
    ("Terminal 1", "Depo 2", 20),
    ("Terminal 1", "Depo 3", 15),
    ("Terminal 2", "Depo 3", 15),
    ("Terminal 2", "Depo 4", 30),
    ("Terminal 2", "Depo 2", 10),
    ("Depo 1", "Store 1", 15),
    ("Depo 1", "Store 2", 10),
    ("Depo 1", "Store 3", 20),
    ("Depo 2", "Store 4", 15),
    ("Depo 2", "Store 5", 10),
    ("Depo 2", "Store 6", 25),
    ("Depo 3", "Store 7", 20),
    ("Depo 3", "Store 8", 15),
    ("Depo 3", "Store 9", 10),
    ("Depo 4", "Store 10", 20),
    ("Depo 4", "Store 11", 10),
    ("Depo 4", "Store 12", 15),
    ("Depo 4", "Store 13", 5),
    ("Depo 4", "Store 14", 10),
]

# creating artificial nodes in order to have all system connected, Sorce on top of the system, sin on the bottom
source = "Source"
sink = "Sink"

# G.add_weighted_edges_from(edges)
G.add_weighted_edges_from(edges, weight="capacity")

terminals = ["Terminal 1", "Terminal 2"]
warehouses = ["Depo 1", "Depo 2", "Depo 3", "Depo 4"]
stores = [
    "Store 1",
    "Store 2",
    "Store 3",
    "Store 4",
    "Store 5",
    "Store 6",
    "Store 7",
    "Store 8",
    "Store 9",
    "Store 10",
    "Store 11",
    "Store 12",
    "Store 13",
    "Store 14",
]

# Add artificial connections from the source to the terminals
for terminal in terminals:
    G.add_edge(source, terminal, capacity=float("inf"))

# Add artificial connections from the stores to the sink
for store in stores:
    G.add_edge(store, sink, capacity=float("inf"))


# calculate the capacity matrix for edmonds-karp algrithm
def capacity_mtx(edges, node_list):
    # as we use names for the graph edges, we need to get indicies of that nodes
    node_indices = {node: i for i, node in enumerate(node_list)}
    num_nodes = len(node_list)
    capacity_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for u, v, capacity in edges:
        capacity_matrix[node_indices[u]][
            node_indices[v]
        ] = capacity  # Assign capacity to directed edge
    return capacity_matrix


node_list = list(G.nodes)  # Get the list of nodes


# cap_matrx = capacity_mtx(edges, nodes)
cap_matrx = capacity_mtx(G.edges(data="capacity"), node_list)

# as we have code implementation of edmonds-karp algorithm, insted of library nx.maximum_flow we need to provide indicies
source_idx = node_list.index(source)
sink_idx = node_list.index(sink)

max_flow, flow_distribution = edmonds_karp(cap_matrx, source_idx, sink_idx)

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, k=0.5, seed=42)
# pos = nx.kamada_kawai_layout(G)


# Draw the base graph
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=1000,
    font_size=10,
    font_color="black",
    arrowsize=20,
    arrowstyle="-|>",
    connectionstyle="arc3,rad=0.2",
)

plt.show()


# report
print(f"🔹 Maximum Flow Through the Network: {max_flow}\n")

flow_summary = defaultdict(dict)

# we are going over flow distribution matrix to retrive flow between Nodes
# and storing them in flow_summary for easy lookup between nodes
for i in range(len(flow_distribution)):
    for j in range(len(flow_distribution[i])):
        flow = flow_distribution[i][j]
        if flow > 0:
            flow_summary[i][j] = flow

for start, destinations in flow_summary.items():
    print(f"\n➡️ {node_list[start]}:")
    for end, flow in destinations.items():
        print(f"    → {node_list[end]}: {flow}")

# Calculate and report utilization
print("\n📈 Edge Utilization:")
for u, v, data in G.edges(data=True):
    capacity = data["capacity"]
    flow = flow_distribution[node_list.index(u)][node_list.index(v)]
    utilization = (flow / capacity) * 100 if capacity > 0 else 0
    print(f"    {u} → {v}: {utilization:.2f}% ({flow}/{capacity})")
