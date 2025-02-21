from collections import deque
from graph import cap_matrx


def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    print("\n BFS Search Started")

    while queue:
        current_node = queue.popleft()
        print(f"Exploring node {current_node}")

        for neighbor in range(len(capacity_matrix)):
            residual_capacity = (
                capacity_matrix[current_node][neighbor]
                - flow_matrix[current_node][neighbor]
            )

            if residual_capacity > 0 and neighbor == sink:
                print(
                    f"⚠️ Found potential sink connection: {current_node} -> {sink}, Capacity: {residual_capacity}"
                )

            if not visited[neighbor] and residual_capacity > 0:
                print(
                    f" ✅ Found edge {current_node} -> {neighbor}, Residual Capacity: {residual_capacity}"
                )

                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    print("✅ Path found to sink!")
                    return True

                queue.append(neighbor)
    print("❌ No path found!")
    return False


def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    parent = [-1] * num_nodes
    max_flow = 0

    iteration = 1

    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        print(f"\n🔄 Iteration {iteration}")
        iteration += 1

        path_flow = float("Inf")
        current_node = sink

        path = []

        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(
                path_flow,
                capacity_matrix[previous_node][current_node]
                - flow_matrix[previous_node][current_node],
            )
            path.append(current_node)
            current_node = previous_node

        path.append(source)  # Include source in the path
        path.reverse()  # Correct order from source to sink
        print(f" Augmenting path: {path[::-1]}, Flow added: {path_flow}")

        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node

        max_flow += path_flow
    # print("\n📊 Final flow matrix:")
    # for row in flow_matrix:
    #     print(row)

    return max_flow


source = 0
sink = 6

print(f"Maximum flow: {edmonds_karp(cap_matrx, source, sink)}")
