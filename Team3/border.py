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

r = None

while True:
    r = random.choice(borders)
    
    if (r == (0, 0) or
        r == (0, size - 1) or
        r == (size - 1, size - 1) or
            r == (size - 1, 0)):
        continue
    
    break

print(borders)

for item in borders:
    b[item] = '#'

b[r] = 'X'

b.draw()
