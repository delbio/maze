from random import randrange
import argparse
from src.maze_value import WALL, EMPTY, ENDING_CELL, VISITED_CELL, STARTING_CELL, HORIZONTAL_PATH, VERTICAL_PATH
from src.generator import generate
from src.find_path_recursive_on_rigth import find_path_recursive_on_rigth
from src.find_path_astar import find_path_astar


#find_path_algorithm = find_path_recursive_on_rigth
find_path_algorithm = find_path_astar

def random_empty_cell_inside_maze(maze):
    pos = (randrange(maze.width), randrange(maze.height))
    cell = maze.get_cell(pos)
    while cell is not EMPTY:
        pos = (randrange(maze.width), randrange(maze.height))
        cell = maze.get_cell(pos)
    return pos

buildstart = random_empty_cell_inside_maze
buildend = random_empty_cell_inside_maze

def solve(maze, get_start, get_goal, find_path):
    start = get_start(maze)
    goal = get_goal(maze)
    print('Start Point: {start} , End Point: {end})'.format(start=start, end=goal))
    path = find_path(maze, start, goal)
    if path == "NO WAY" :
        path = None
    return maze, start, goal, path

def add_visited_cell_to_maze(maze, visited):
    if visited is None:
        pass
    for pos in visited:
        maze.set_cell(pos, VISITED_CELL)

def set_path_to_maze(maze, start, goal, path):
    current = start
    move = {"S": (1,0), "N": (-1,0), "W": (0,-1), "E": (0, 1)}
    cell_value = {"S": VERTICAL_PATH, "N": VERTICAL_PATH, "W": HORIZONTAL_PATH, "E": HORIZONTAL_PATH}
    for direction in path:
        x, y = current
        move_x, move_y = move[direction]
        current = (x + move_x, y + move_y)
        maze.set_cell(current, cell_value[direction])
    pass

def popolate_maze_with_path(maze, start, goal, path):
    if path is not None:
        print('\nFounded path to end\n')
        try:
            if isinstance(path, str):
                set_path_to_maze(maze,start,goal,path)
            else:
                add_visited_cell_to_maze(maze,path)
        except IndexError as e:
            print('path: {path}, pos: {pos} , maze: {maze}'.format(path=path,pos=pos,maze=maze.value))
            raise
    else:
        print('\nNo path founded for end\n')
    maze.set_cell(goal, ENDING_CELL)
    maze.set_cell(start, STARTING_CELL)



def display(args):
    maze, start, goal, path = args
    popolate_maze_with_path(maze, start, goal, path)
    char_mapping = {
            WALL: '#',
            EMPTY: ' ',
            ENDING_CELL: 'E',
            VISITED_CELL: '.',
            HORIZONTAL_PATH: '-',
            VERTICAL_PATH: '|',
            STARTING_CELL: 'S'
    }
    for row in reversed(maze.value):
        maze_row = ""
        for cell in row:
            maze_row += char_mapping[cell]
        print(maze_row)

def maze(width, height, wall_density):
    display(solve(generate(width, height, wall_density), buildstart, buildend, find_path_algorithm))

def getArgs():
    parser = argparse.ArgumentParser(description='CLI Maze')
    parser.add_argument('cols', type=int, help='number of columns')
    parser.add_argument('rows', type=int, help='number of rows')
    parser.add_argument('wall_density', type=float, help='wall density')
    return parser.parse_args()

if __name__ == '__main__':
    args = getArgs()
    print('Try to solve maze with: {cols} cols, {rows} rows, {density}% of wall'.format(cols=args.cols, rows=args.rows, density=(int(args.wall_density*100)))) 
    try:
        maze(args.cols, args.rows, args.wall_density)
    except ValueError as e:
        print('Not valid Parameter: ', str(e))

