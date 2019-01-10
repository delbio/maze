from .maze_value import WALL, EMPTY, ENDING_CELL, VISITED_CELL, STARTING_CELL

def find_path_recursive_on_rigth(maze, start, goal):
    visited = set()
    def find_path(maze, current):
        try:
            if current == goal:
                #print('found at', x, ',', y)
                return True
            elif maze.get_cell(current) == WALL:
                #print('wall at', x, ',', y)
                return False
            elif current in visited:
                #print('visited at', x, ',', y)
                return False
            
            #print('visiting at', x, ',', y)

            # mark as visited
            visited.add(current)

            # explore neighbors clockwise starting by the one on the right
            x, y = current
            if ((x < maze.width-1 and find_path(maze, (x+1, y)))
                or (y > 0 and find_path(maze, (x, y-1)))
                or (x > 0 and find_path(maze, (x-1, y)))
                or (y < maze.height-1 and find_path(maze, (x, y+1)))):
                return True

            return False
        except IndexError:
            print('search {pos} into: {maze}'.format(pos=current,maze=maze.value))
            raise

    founded = find_path(maze, start)
    if founded:
        return visited
    else:
        return "NO WAY"

