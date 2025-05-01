import heapq


def dijkstra(graph, start):
    """Dijkstra's algorithm to find the shortest path from the start node to all other nodes."""
    n = len(graph)
    distances = [float('inf')] * n
    priority_queue = [(0, start)]
    distances[start] = 0

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def build_graph():
    """Accepts user input to build the graph."""
    n = int(input("Enter the number of vertices: "))
    m = int(input("Enter the number of edges: "))
    graph = [[] for _ in range(n)]

    print("Enter the edges in the format: source destination weight")
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph


def main():
    """Main function to run the Dijkstra's algorithm."""
    graph = build_graph()
    start = int(input("Enter the starting vertex: "))
    distances = dijkstra(graph, start)

    print(f"Shortest distances from vertex {start}:")
    for i, d in enumerate(distances):
        print(f"Vertex {i}: {d}")


if __name__ == "__main__":
    main()
