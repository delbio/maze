
WALL = 1
EMPTY = 0
ENDING_CELL = 2
VISITED_CELL = 3
STARTING_CELL = 4

class Maze():
    def __init__(self, width, height, init_value):
        self.width = width
        self.height = height
        self.value = [ [ init_value ] * self.width for _ in range(self.height) ]

    def set_cell(self, position, value):
        """
        @param position: (x,y)
        @param value: 
        """
        self.value[position[1]][position[0]] = value

    def get_cell(self, position):
        """
        @param position: (x,y)
        @return value of cell or raise IndexError
        """
        return self.value[position[1]][position[0]]



