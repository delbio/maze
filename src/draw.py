from .models import WALL, EMPTY
from .a_star_search import reconstruct_path, end_reached


START           = 100
GOAL            = 200
HORIZONTAL_PATH = 300
VERTICAL_PATH   = 400

CHAR_MAPPING = {
        WALL: '#',
        EMPTY: ' ',
        GOAL: 'E',
        HORIZONTAL_PATH: '-',
        VERTICAL_PATH: '|',
        START: 'S'
}

def draw_tile_start(graph, id, width, came_from, **option):
    return CHAR_MAPPING[START]

def draw_tile_end(graph, id, width, came_from, **option):
    return CHAR_MAPPING[GOAL]

def draw_tile_wall(graph, id, width, came_from, **option):
    return CHAR_MAPPING[WALL] * width

def draw_tile_path_direction(graph, id, width, came_from, **option):
    if came_from.get(id, None) is not None:
        x1, y1 = id
        x2, y2 = came_from[id]
        if x2 == x1 + 1 or x2 == x1 -1 : return CHAR_MAPPING[HORIZONTAL_PATH] 
        if y2 == y1 + 1 or y2 == y1 -1 : return CHAR_MAPPING[VERTICAL_PATH]
    else:
        return CHAR_MAPPING[EMPTY]

def draw_tile(graph, id, width, came_from, **option):
    if graph.get_cell(id) == WALL: return draw_tile_wall(graph, id, width, came_from, **option)
    if 'start' in option and id == option['start']: return draw_tile_start(graph, id, width, came_from, **option) 
    if 'goal' in option and id == option['goal']: return draw_tile_end(graph, id, width, came_from, **option) 
    return draw_tile_path_direction(graph, id, width, came_from, **option)

def draw_grid(args):
    maze, start, goal, came_from, cost_so_far = args
    cell_width = 1
    print('Start Point: {start} , End Point: {end})'.format(start=start, end=goal))
    if end_reached(came_from, start, goal):
        print('\nFounded path to end\n')
    else:
        print('\nNo path founded for end\n')

    for y in range(maze.height):
        for x in range(maze.width):
            print("%%-%ds" % cell_width % draw_tile(maze, (x, y), cell_width, came_from, start=start, goal=goal), end="")
        print()
