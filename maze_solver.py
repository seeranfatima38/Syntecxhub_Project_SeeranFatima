import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(maze, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        # path logic (fixed indentation only)
        path = []
        temp = current
        while temp:
            path.append(temp.position)
            temp = temp.parent

        if current.position == goal:
            return path[::-1]

        closed_set.add(current.position)

        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

        for move in neighbors:
            node_pos = (
                current.position[0] + move[0],
                current.position[1] + move[1]
            )

            # boundary check (needed or it crashes)
            if (node_pos[0] < 0 or node_pos[0] >= len(maze) or
                node_pos[1] < 0 or node_pos[1] >= len(maze[0])):
                continue

            if maze[node_pos[0]][node_pos[1]] == '#':
                continue

            if node_pos in closed_set:
                continue

            neighbor = Node(node_pos, current)

            neighbor.g = current.g + 1
            neighbor.h = heuristic(node_pos, goal)
            neighbor.f = neighbor.g + neighbor.h

            heapq.heappush(open_list, neighbor)  # fixed spelling

    return None


maze = [
    ['S', '.', '.', '#'],
    ['#', '.', '.', '#'],
    ['#', '.', 'G', '.']
]

start = (0, 0)
goal = (2, 2)

path = astar(maze, start, goal)

def print_maze_with_path(maze, path):
    maze_copy = [row[:] for row in maze]

    for (x, y) in path:
        if maze_copy[x][y] not in ('S', 'G'):
            maze_copy[x][y] = '*'

    for row in maze_copy:
        print(' '.join(row))


if path:
    print("Path found:", path)
    print("\nMaze with path:\n")
    print_maze_with_path(maze, path)
else:
    print("No path found")
