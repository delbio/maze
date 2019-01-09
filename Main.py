from random import randrange
import argparse


WALL = 1
EMPTY = 0
ENDING_CELL = 2
VISITED_CELL = 3
STARTING_CELL = 4

def generate(width, height, wall_density):
    """
    Attributes:
        width (int): number of columns
        height (int): number of rows
        wall_density (float): density of wall in percentage
    """
    num_cells = width * height
    # Create maze full of wall
    maze = [ [ WALL ] * width for _ in range(height) ]
    num_wall_cells_to_remove = num_cells - int(num_cells * wall_density)
    # Remove num_wall_cells Wall to have maze with wall_density wall cell
    while num_wall_cells_to_remove > 0:
        # Get random cell inside maze
        col = randrange(width)
        row = randrange(height)
        try:
            cell = maze[col][row]
            if cell == WALL:
                maze[col][row] = EMPTY
                num_wall_cells_to_remove -= 1
        except IndexError:
            print(col, row, maze)
            raise
 
    return maze

def search(grid, x, y):
    if grid[x][y] == ENDING_CELL:
        #print('found at', x, ',', y)
        return True
    elif grid[x][y] == WALL:
        #print('wall at', x, ',', y)
        return False
    elif grid[x][y] == VISITED_CELL:
        #print('visited at', x, ',', y)
        return False
    
    #print('visiting at', x, ',', y)

    # mark as visited
    grid[x][y] = VISITED_CELL

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(grid)-1 and search(grid, x+1, y))
        or (y > 0 and search(grid, x, y-1))
        or (x > 0 and search(grid, x-1, y))
        or (y < len(grid)-1 and search(grid, x, y+1))):
        return True

    return False

def random_empty_cell_inside_maze(maze):
    cols = len(maze[0])
    rows = len(maze)
    x = randrange(cols)
    y = randrange(rows)
    cell = maze[x][y]
    while cell is not EMPTY:
        x = randrange(cols)
        y = randrange(rows)
        cell = maze[x][y]
    return ( x, y )

buildstart = random_empty_cell_inside_maze
buildend = random_empty_cell_inside_maze

def solve(maze, start, end):
    sx, sy = start(maze)
    ex, ey = end(maze)
    maze[ex][ey] = ENDING_CELL
    #display(maze)
    #print('start: ( ',sx,',',sy,' )',' end: ( ',ex,',',ey,' )')
    search(maze, sx, sy)
    maze[sx][sy] = STARTING_CELL
    return maze

def display(maze):
    char_mapping = {
            WALL: '#',
            EMPTY: ' ',
            ENDING_CELL: 'E',
            VISITED_CELL: '.',
            STARTING_CELL: 'O'
    }
    for row in maze:
        maze_row = ""
        for cell in row:
            maze_row += char_mapping[cell]
        print(maze_row)

def maze(width, height, wall_density):
    display(solve(generate(width, height, wall_density), buildstart, buildend))
    #display(generate(width, height, wall_density))

def getArgs():
    parser = argparse.ArgumentParser(description='CLI Maze')
    parser.add_argument('cols', type=int, help='number of columns', default=10 )
    parser.add_argument('rows', type=int, help='number of rows', default=10 )
    parser.add_argument('wall_density', type=float, help='wall density', default=.25)
    return parser.parse_args()

if __name__ == '__main__':
    args = getArgs()
    
    print(args.cols, args.rows, args.wall_density)
    maze(args.cols, args.rows, args.wall_density)

