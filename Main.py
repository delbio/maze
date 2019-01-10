from random import randrange
import argparse
from src.maze_value import WALL, EMPTY, ENDING_CELL, VISITED_CELL, STARTING_CELL
from src.generator import generate
from src.find_path_recursive_on_rigth import find_path_recursive_on_rigth
from src.find_path_astar import find_path_astar


find_path = find_path_recursive_on_rigth

def random_empty_cell_inside_maze(maze):
    pos = (randrange(maze.width), randrange(maze.height))
    cell = maze.get_cell(pos)
    while cell is not EMPTY:
        pos = (randrange(maze.width), randrange(maze.height))
        cell = maze.get_cell(pos)
    return pos

buildstart = random_empty_cell_inside_maze
buildend = random_empty_cell_inside_maze

def solve(maze, get_start, get_goal):
    start = get_start(maze)
    goal = get_goal(maze)
    print('Start Point: {start} , End Point: {end})'.format(start=start, end=goal))
    path = find_path(maze, start, goal)
    if path == "NO WAY" :
        path = None
    return maze, start, goal, path

def display(args):
    maze, start, goal, path = args

    if path is not None:
        print('\nFounded path to end\n')
        for pos in path: 
            maze.set_cell(pos, VISITED_CELL)
    else:
        print('\nNo path founded for end\n')
    maze.set_cell(goal, ENDING_CELL)
    maze.set_cell(start, STARTING_CELL)

    char_mapping = {
            WALL: '#',
            EMPTY: ' ',
            ENDING_CELL: 'E',
            VISITED_CELL: '.',
            STARTING_CELL: 'S'
    }
    for row in reversed(maze.value):
        maze_row = ""
        for cell in row:
            maze_row += char_mapping[cell]
        print(maze_row)

def maze(width, height, wall_density):
    display(solve(generate(width, height, wall_density), buildstart, buildend))

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

