import random

from board import Empty

def add_wall(b):
    walls = list(b.iterdata())

    while True:
        start_coord, _ = random.choice(walls)

        if not b.is_corner(start_coord):
            break

    if b.is_edge(start_coord):

        v = []
        for dim, c in enumerate(start_coord):
            if c == 0:
                v.append(1)
            elif c == len(b.dimensions[dim]):
                v.append(-1)
            else:
                v.append(0)

    else:
        v = [random.choice([1, -1]), 0]
        random.shuffle(v)

    start_coord = tuple(
        x + d for x, d in zip(start_coord, v)
    )

    length = random.randint(len(b.dimensions[0]))

    for l, coord in enumerate(b.iterline(start_coord, v)):
        if l >= length:
            break

        if b[coord] is Empty:
            b[coord] = '#'
        else:
            break


def make_walls(board, num_walls=None):
    num_walls = 10

    for i in range(num_walls):
        add_wall(board)
