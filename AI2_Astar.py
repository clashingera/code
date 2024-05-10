import heapq
import math

class Cell:
    def __init__(self, parent_i=0, parent_j=0, f=float('inf'), g=float('inf'), h=0):
        self.parent_i = parent_i
        self.parent_j = parent_j
        self.f = f
        self.g = g
        self.h = h

def is_valid(row, col):
    return 0 <= row < ROW and 0 <= col < COL

def is_unblocked(grid, row, col):
    return grid[row][col] == 1

def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

def calculate_h_value(row, col, dest):
    return math.sqrt((row - dest[0]) ** 2 + (col - dest[1]) ** 2)

def trace_path(cell_details, dest):
    path = []
    row, col = dest
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        row, col = cell_details[row][col].parent_i, cell_details[row][col].parent_j
    path.append((row, col))
    path.reverse()
    print("The Path is:", path)

def a_star_search(grid, src, dest):
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid")
        return

    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        print("Source or the destination is blocked")
        return

    if is_destination(src[0], src[1], dest):
        print("We are already at the destination")
        return

    closed_list = [[False] * COL for _ in range(ROW)]
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    i, j = src
    cell_details[i][j] = Cell(i, j, 0, 0, 0)
    open_list = [(0.0, i, j)]

    while open_list:
        f, i, j = heapq.heappop(open_list)

        closed_list[i][j] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i, new_j = i + dir[0], j + dir[1]

            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                if is_destination(new_i, new_j, dest):
                    cell_details[new_i][new_j] = Cell(i, j, 0, 0, 0)
                    print("The destination cell is found")
                    trace_path(cell_details, dest)
                    return
                else:
                    g_new = cell_details[i][j].g + 1.0
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        cell_details[new_i][new_j] = Cell(i, j, f_new, g_new, h_new)

    print("Failed to find the destination cell")

def main():
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    src = (8, 0)
    dest = (0, 0)

    a_star_search(grid, src, dest)

if __name__ == "__main__":
    ROW, COL = 9, 10
    main()

'''
Certainly! Let's break down the code and the output:

1. **Code Explanation**:
    - The code defines a simplified version of the A* algorithm to find the shortest path from a given source cell to a destination cell on a grid.
    - It uses the `Cell` class to represent each cell in the grid, containing information about its parent cell, the cost from the start cell to the current cell (`g`), the heuristic cost from the current cell to the destination cell (`h`), and the total cost (`f`) which is the sum of `g` and `h`.
    - The `is_valid`, `is_unblocked`, and `is_destination` functions check whether a given cell is within the grid boundaries, unblocked, and the destination, respectively.
    - The `calculate_h_value` function calculates the heuristic (Euclidean distance) from a given cell to the destination cell.
    - The `trace_path` function traces the path from the destination cell back to the source cell using the information stored in the `cell_details`.
    - The `a_star_search` function implements the A* algorithm to search for the shortest path from the source to the destination cell.
    - Finally, the `main` function defines the grid, source, and destination, and calls the `a_star_search` function to find the path.

2. **Output Explanation**:
    - The output indicates that the destination cell is found.
    - The path from the source `(8, 0)` to the destination `(0, 0)` is printed. The path is: `[(8, 0), (7, 0), (6, 0), (5, 0), (4, 1), (3, 2), (2, 1), (1, 0), (0, 0)]`.
    - Each tuple in the path represents the row and column indices of the cells in the path, starting from the source and ending at the destination.

Overall, the code successfully finds the shortest path from the source to the destination on the given grid using the A* algorithm.
'''


'''
another one
def aStarAlgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {start_node: 0}  # store distance from starting node
    parents = {start_node: start_node}  # parents contain an adjacency map of all nodes

    while open_set:
        n = min(open_set, key=lambda x: g[x] + heuristic(x))

        if n == stop_node or n not in Graph_nodes:
            break

        for m, weight in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            elif g[m] > g[n] + weight:
                g[m] = g[n] + weight
                parents[m] = n
                if m in closed_set:
                    closed_set.remove(m)
                    open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    if n != stop_node:
        print('Path does not exist!')
        return None

    # Reconstruct path
    path = []
    while n != start_node:
        path.append(n)
        n = parents[n]
    path.append(start_node)
    path.reverse()

    print('Path found:', path)
    return path

def get_neighbors(v):
    return Graph_nodes[v] if v in Graph_nodes else []

def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist.get(n, float('inf'))

Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('G', 9)],
    'C': [('B', 1)],
    'D': [('E', 6), ('G', 1)],
    'E': [('A', 3), ('D', 6)],
    'G': [('B', 9), ('D', 1)]
}

aStarAlgo('A', 'G')


'''