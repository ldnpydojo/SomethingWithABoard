import os, sys
import random

import board
import border
import walls
import solver

def main(size=10):
    size = int(size)
    maze = board.Board((size, size))
    exit_coord = border.make_borders(maze)
    walls.make_walls(maze)

    empty_coords = [coord for coord in maze if maze[coord] is board.Empty]
    start_coord = random.choice(empty_coords)
    print("Start at", start_coord)
    print("Exit at", exit_coord)
    maze[start_coord] = "O"
    maze.draw()
    solver.solve_maze(maze, start_coord, exit_coord)

if __name__ == '__main__':
    main(*sys.argv[1:])
