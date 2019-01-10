def maze2graph(maze):
    height = maze.height
    width = maze.width if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze.value[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze.value[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze.value[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph
