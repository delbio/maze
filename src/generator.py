from random import randrange
from .models import Maze, WALL, EMPTY


def generate(width, height, wall_density):
    if width <= 0:
        raise ValueError('number of columns must be greater than 0')
    if height <= 0:
        raise ValueError('number of rows must be greater than 0')
    if (wall_density < 0) or (wall_density > 1):
        raise ValueError('wall_density must be float value between 0 and 1')
    num_cells = width * height
    num_wall_cells_to_remove = num_cells - int(num_cells * wall_density)
    # Create maze full of wall
    maze = Maze(width, height, WALL)
    # Remove num_wall_cells Wall to have maze with wall_density wall cell
    while num_wall_cells_to_remove > 0:
        # Get random cell inside maze
        pos = (randrange(width), randrange(height))
        try:
            cell = maze.get_cell(pos)
            if cell == WALL:
                maze.set_cell(pos, EMPTY)
                num_wall_cells_to_remove -= 1
        except IndexError:
            print('cell {pos} grid_size: ( w: {w} , h: {h} ) into: {grid}'.format(pos=pos, w=maze.width, h=maze.height, grid=maze.value))
            raise
 
    return maze

