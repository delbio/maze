from random import randrange

WALL = 1
EMPTY = 0

class SquareGrid:
    def __init__(self, width, height, init_value):
        """
        @param width
        @param height
        @param init_value 
        """
        self.width = width
        self.height = height
        self.value = [ [ init_value ] * self.width for _ in range(self.height) ]

    def set_cell(self, position, value):
        """
        @param position: (x,y)
        @param value: 
        """
        (x, y) = position
        self.value[y][x] = value

    def get_cell(self, position):
        """
        @param position: (x,y)
        @return value of cell or raise IndexError
        """
        (x, y) = position
        return self.value[y][x]

class Graph(SquareGrid):
    def __init__(self, width, height, init_value):
        super().__init__(width, height, init_value)
        self.graph = None

    def _build_empty_graph(self):
        # Build an empty graph will all reachable node and all connection as non calculated
        self.graph = {(x, y): None for y in range(self.height) for x in range(self.width) if not (self.value[y][x] == WALL)}

    def get_all_nodes(self):
        """
        return all reachable node into the maze
        """
        if self.graph is None:
            self._build_empty_graph()
        return self.graph.keys()

    def neighbords(self, node):
        if self.graph is None:
            self._build_empty_graph()
        x, y = node
        if self.graph[(x,y)] is None:
            dirs = [
                    [1, 0], # right
                    [0, 1], # up
                    [-1, 0],# left
                    [0, -1] # down
                    ]
            results = []
            all_nodes = self.graph.keys()
            for direction in dirs:
                neighbord = (x + direction[0], y + direction[1])
                if neighbord in all_nodes:
                    results.append(neighbord)
            self.graph[(x,y)] = results
        return self.graph[(x,y)]

class GraphWithWeights(Graph):
    def __init__(self, width, height, init_value):
        super().__init__(width, height, init_value)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

class Maze(GraphWithWeights):
    def __init__(self, width, height, init_value):
        super().__init__(width, height, init_value)

def random_empty_cell_inside_grid(maze):
    pos = (randrange(maze.width), randrange(maze.height))
    cell = maze.get_cell(pos)
    while cell is not EMPTY:
        pos = (randrange(maze.width), randrange(maze.height))
        cell = maze.get_cell(pos)
    return pos

