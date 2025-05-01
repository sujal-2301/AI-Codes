import heapq


class Node:
    def __init__(self, position, g, h):
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f


def astar(start, goal, grid):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, Node(start, 0, heuristic(start, goal)))

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.position)

        for neighbor in get_neighbors(current_node.position, grid):
            if neighbor in closed_list:
                continue

            g_cost = current_node.g + 1
            h_cost = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, g_cost, h_cost)
            neighbor_node.parent = current_node

            if not any(neighbor_node.position == node.position and neighbor_node.f < node.f for node in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(position, grid):
    x, y = position
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            neighbors.append((nx, ny))

    return neighbors


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter the grid (0 for empty, 1 for obstacle):")
    grid = []
    for i in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)

    start_x, start_y = map(int, input("Enter start position (x y): ").split())
    goal_x, goal_y = map(int, input("Enter goal position (x y): ").split())

    start = (start_x, start_y)
    goal = (goal_x, goal_y)

    path = astar(start, goal, grid)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")


# Run the program
main()
