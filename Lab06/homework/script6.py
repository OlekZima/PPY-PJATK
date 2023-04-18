def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    visited = set()

    while len(visited) < len(graph):
        current_node = min({node: distance for (node, distance) in distances.items() if node not in visited},
                           key=distances.get)

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances


graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 2},
    'C': {'A': 1, 'B': 2}
}

print(dijkstra(graph, 'A'))
