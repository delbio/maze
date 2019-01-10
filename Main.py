import argparse
from src.generator import generate
from src.models import random_empty_cell_inside_grid
from src.a_star_search import a_star_search
from src.draw import draw_grid


buildstart = random_empty_cell_inside_grid
buildend = random_empty_cell_inside_grid

def solve(maze, get_start, get_goal, find_path):
    start = get_start(maze)
    goal = get_goal(maze)
    came_from, cost_so_far = find_path(maze, start, goal)
    return maze, start, goal, came_from, cost_so_far

def maze(width, height, wall_density):
    draw_grid(solve(generate(width, height, wall_density), buildstart, buildend, a_star_search))

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

