import random
from board import Board

size = 10

b = Board((size, size))
b.populate(' ' * (size * size))

borders = []

borders += list(b.iterline((0, 1), (0, 1)))
borders += list(b.iterline((size - 2, 0), (-1, 0)))
borders += list(b.iterline((size - 1, size - 2), (0, -1)))
borders += list(b.iterline((1, size - 1), (1, 0)))
r = random.randint(0, len(borders) - 1)

print(borders)

for item in borders:
    b[item] = '#'

b[borders[r]] = 'X'

b.draw()
