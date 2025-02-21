import networkx as nx

# Create graph that represents structure in task
G = nx.DiGraph()

edges = [
    (0, 2, 25),  # terminal 1 -> depot 1
    (0, 3, 20),  # terminal 1 -> depot 2
    (0, 4, 15),  # terminal 1 -> depot 3
    (1, 4, 15),  # terminal 2 -> depot 3
    (1, 5, 30),  # terminal 2 -> depot 4
    (1, 3, 10),  # terminal 2 -> depot 2
    (2, 6, 15),  # depot1 -> store 1
    (2, 7, 10),  # depot 1 -> store 2
    (2, 8, 20),  # depot 1 -> store 3
    (3, 9, 15),  # depot 2 -> store 4
    (3, 10, 10),  # depot 2 -> store 5
    (3, 11, 25),  # depot 2 -> store 6
    (4, 12, 20),  # depot 3 -> store 7
    (4, 13, 15),  # depot 3 -> store 8
    (4, 14, 10),  # depot 3 -> store 9
    (5, 15, 20),  # depot 4 -> store 10
    (5, 16, 10),  # depot 4 -> store 11
    (5, 17, 15),  # depot 4 -> store 12
    (5, 18, 5),  # depot 4 -> store 13
    (5, 19, 10),  # depot 4 -> store 14
]


G.add_weighted_edges_from(edges, weight="capacity")

num_nodes = len(G.nodes)


def capacity_mtx(edges, num_nodes):
    capacity_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for u, v, capacity in edges:
        capacity_matrix[u][v] = capacity  # Assign capacity to directed edge
    return capacity_matrix


cap_matrx = capacity_mtx(edges, num_nodes)
