from collections import deque

# Graph Representation (Adjacency List)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Add an edge between nodes u and v"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start, visited=None):
        """Recursive Depth First Search (DFS)"""
        if visited is None:
            visited = set()

        # Visit the node
        visited.add(start)
        print(start, end=" ")

        # Visit all unvisited neighbors
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        """Iterative Breadth First Search (BFS)"""
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            # Visit all unvisited neighbors
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Create a Graph and add edges
g = Graph()

# Adding edges to the graph (undirected graph)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

# Perform DFS Traversal
print("DFS Traversal (starting from node 0):")
g.dfs(0)  # Depth First Search

# Perform BFS Traversal
print("\nBFS Traversal (starting from node 0):")
g.bfs(0)  # Breadth First Search
