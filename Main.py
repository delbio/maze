def start(maze):
    raise NotImplementedError

def end(maze):
    raise NotImplementedError

def generate(width, height, wall_density):
    raise NotImplementedError

def solve(maze, start, end):
    raise NotImplementedError

def display(maze):
    raise NotImplementedError

def maze(width, height, wall_density):
    display(solve(generate(width, height, wall_density), start, end))

if __name__ == '__main__':
    maze(10, 10, .75)

