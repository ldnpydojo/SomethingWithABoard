import random
from board import Board

size = 10

def make_borders(b):

    borders = []

    borders += list(b.iterline((0, 1), (0, 1)))
    borders += list(b.iterline((size - 2, 0), (-1, 0)))
    borders += list(b.iterline((size - 1, size - 2), (0, -1)))
    borders += list(b.iterline((1, size - 1), (1, 0)))

    for item in borders:
        b[item] = '#'

    while True:
        r = random.choice(borders)
        if not b.is_corner(r):
            b[r] = 'X'
            return r

if __name__ == '__main__':
    b = Board((size, size))
    make_borders(b)
    b.draw()
