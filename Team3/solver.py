import board
from board import Empty

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


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


def search(b, node, destination, visited=None, path=None):
    if visited is None:
        visited = []
    if path is None:
        path = []

    if node == destination:
        return path

    visited.append(node)

    for connected in get_neighbours(node, b):
        if connected not in visited:
            path.append(connected)
            result = search(b, connected, destination, visited, path)
            if result:
                return result
            del path[-1]

def solve_maze(maze, entrance, exit):
    path = search(maze, entrance, exit)
    maze[entrance] = 0

    if path is not None:
        for i, coord in enumerate(path):
            maze[coord] = i + 1
        maze.draw()
    else:
        print('There is no solution!')


if __name__ == '__main__':
    b = board.Board((5, 5))
    b.populate(Empty for _ in range(100))

    b[2, 1] = 'X'
    b[2, 2] = 'X'
    b[2, 3] = 'X'
    b[2, 4] = 'X'
    
    solve_maze(b, (0, 4), (4, 4))

    

    
