from random import randrange

def start(maze):
    raise NotImplementedError

def end(maze):
    raise NotImplementedError

WALL = 1
EMPTY = 0

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
        cell = maze[col][row]
        if cell == WALL:
            maze[col][row] = EMPTY
            num_wall_cells_to_remove -= 1
 
    return maze

def solve(maze, start, end):
    raise NotImplementedError

def display(maze):
    char_mapping = {
            WALL: '#',
            EMPTY: ' '
    }
    for row in maze:
        maze_row = ""
        for cell in row:
            maze_row += char_mapping[cell]
        print(maze_row)

def maze(width, height, wall_density):
    #display(solve(generate(width, height, wall_density), start, end))
    display(generate(width, height, wall_density))

if __name__ == '__main__':
    maze(10, 10, .75)

