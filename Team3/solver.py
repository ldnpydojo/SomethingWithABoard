import board
from board import Empty
from math import sqrt

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def get_neighbours(coord, b):
    x = coord[0]
    y = coord[1]
    
    neighbours = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]

    return [coord for coord in neighbours if coord in b and b[coord] != '#']


def search(b, node, destination, visited=None, path=None, heuristic=None):
    if visited is None:
        visited = []
    if path is None:
        path = []

    if node == destination:
        return path

    visited.append(node)

    if heuristic is not None:
        neighbours = sorted(get_neighbours(node, b), key=lambda n: heuristic(n, destination))
    else:
        neighbours = get_neighbours(node, b)

    for connected in neighbours:
        if connected not in visited:
            path.append(connected)
            result = search(b, connected, destination, visited, path, heuristic)
            if result:
                return result
            del path[-1]

def solve_maze(maze, entrance, exit):
    heuristics = {
        'dfs': None,
        'dfs_euclidean': euclidean_distance,
        'dfs_manhattan': manhattan_distance, 
    }

    for h in heuristics:
        m = maze.copy()
        print(f'using {h}')
        print(heuristics[h])
        path = search(maze, entrance, exit, heuristic=heuristics[h])
        m[entrance] = 0

        if path is not None:
            for i, coord in enumerate(path):
                m[coord] = i + 1
            m.draw()
        else:
            print('There is no solution!')


if __name__ == '__main__':
    b = board.Board((5, 5))
    b.populate(Empty for _ in range(100))

    b[2, 1] = '#'
    b[2, 2] = '#'
    b[2, 3] = '#'
    b[2, 4] = '#'
    
    solve_maze(b, (0, 4), (4, 4))

    

    
