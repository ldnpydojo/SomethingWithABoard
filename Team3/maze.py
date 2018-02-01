import board
import border
import walls

def main(size=10):
    size = int(size)
    board = board.Board((size, size))
    border.make_borders(board)
    walls.make_walls(board)
