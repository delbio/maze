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

    add_wall = {
            'num_cell_to_modify': int(num_cells * wall_density),
            'default_cell_value': EMPTY,
            'new_value_to_set': WALL
    }
    remove_wall = {
            'num_cell_to_modify': num_cells - int(num_cells * wall_density),
            'default_cell_value': WALL,
            'new_value_to_set': EMPTY
    }

    config = add_wall
    if wall_density > .50:
        config = remove_wall

    # Create maze full of default value
    maze = Maze(width, height, config['default_cell_value'])
    # Remove num_wall_cells Wall to have maze with wall_density wall cell

    while config['num_cell_to_modify'] > 0:
        # Get random cell inside maze
        pos = (randrange(width), randrange(height))
        try:
            cell = maze.get_cell(pos)
            if cell == config['default_cell_value']:
                maze.set_cell(pos, config['new_value_to_set'])
                config['num_cell_to_modify'] -= 1
        except IndexError:
            print('cell {pos} grid_size: ( w: {w} , h: {h} ) into: {grid}'.format(pos=pos, w=maze.width, h=maze.height, grid=maze.value))
            raise
 
    return maze

