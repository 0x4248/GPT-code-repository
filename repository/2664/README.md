# Maze Generator and Solver - 2664

**Language**: `Python`

**Lines of code**: `98`

## Description

This program generates a maze and solves it using two different algorithms - depth-first search and breadth-first search. It allows the user to choose the size of the maze and the starting and ending points.

The program defines a `Maze` class that represents a rectangular grid of cells, each of which may have walls on their four sides. The program generates a maze using a randomized depth-first search algorithm that starts at a given cell and visits each unvisited neighbor of the current cell, carving passages through walls to connect them. Once the algorithm reaches the end cell, it stops. The program also includes two maze solving algorithms - depth-first search and breadth-first search - that take a start and end cell and return a path from the start to the end cell. The `solve_dfs` function uses a stack to keep track of cells to visit and the path taken to reach each cell, while the `solve_bfs` function uses a queue to visit cells in a breadth-first manner.

To test the program, the main function generates a 10x10 maze, prints it to the console, and then solves it using both algorithms, printing the resulting paths to the console.

## Code

``` Python
import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[{"walls": [True, True, True, True], "visited": False} for j in range(width)] for i in range(height)]
    
    def __str__(self):
        output = " " + "_" * (2 * self.width - 1) + "\n"
        for i in range(self.height):
            row_top = "|"
            row_bottom = "+"
            for j in range(self.width):
                if self.grid[i][j]["walls"][0]:
                    row_top += " |"
                else:
                    row_top += "  "
                if self.grid[i][j]["walls"][1]:
                    row_bottom += "-+"
                else:
                    row_bottom += " +"
            output += row_top + "\n"
            output += row_bottom + "\n"
        return output
    
    def generate(self, start=(0, 0), end=None):
        stack = [start]
        self.grid[start[1]][start[0]]["visited"] = True
        while stack:
            current = stack[-1]
            neighbors = []
            if current[0] > 0 and not self.grid[current[1]][current[0]-1]["visited"]:
                neighbors.append((current[0]-1, current[1]))
            if current[0] < self.width-1 and not self.grid[current[1]][current[0]+1]["visited"]:
                neighbors.append((current[0]+1, current[1]))
            if current[1] > 0 and not self.grid[current[1]-1][current[0]]["visited"]:
                neighbors.append((current[0], current[1]-1))
            if current[1] < self.height-1 and not self.grid[current[1]+1][current[0]]["visited"]:
                neighbors.append((current[0], current[1]+1))
            if neighbors:
                next_cell = random.choice(neighbors)
                if next_cell[0] < current[0]:
                    self.grid[current[1]][current[0]]["walls"][3] = False
                    self.grid[next_cell[1]][next_cell[0]]["walls"][1] = False
                elif next_cell[0] > current[0]:
                    self.grid[current[1]][current[0]]["walls"][1] = False
                    self.grid[next_cell[1]][next_cell[0]]["walls"][3] = False
                elif next_cell[1] < current[1]:
                    self.grid[current[1]][current[0]]["walls"][0] = False
                    self.grid[next_cell[1]][next_cell[0]]["walls"][2] = False
                elif next_cell[1] > current[1]:
                    self.grid[current[1]][current[0]]["walls"][2] = False
                    self.grid[next_cell[1]][next_cell[0]]["walls"][0] = False
                stack.append(next_cell)
                self.grid[next_cell[1]][next_cell[0]]["visited"] = True
                if end and next_cell == end:
                    return
            else:
                stack.pop()
    
    def solve_dfs(self, start=(0, 0), end=None):
        stack = [(start, [start])]
        while stack:
    current, path = stack.pop()
    if current == end:
        return path
    for neighbor in self.get_neighbors(current):
        if neighbor not in path:
            stack.append((neighbor, path + [neighbor]))

def solve_bfs(self, start=(0, 0), end=None):
    queue = [(start, [start])]
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        for neighbor in self.get_neighbors(current):
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

def get_neighbors(self, cell):
    neighbors = []
    if cell[0] > 0 and not self.grid[cell[1]][cell[0]]["walls"][3]:
        neighbors.append((cell[0]-1, cell[1]))
    if cell[0] < self.width-1 and not self.grid[cell[1]][cell[0]]["walls"][1]:
        neighbors.append((cell[0]+1, cell[1]))
    if cell[1] > 0 and not self.grid[cell[1]][cell[0]]["walls"][0]:
        neighbors.append((cell[0], cell[1]-1))
    if cell[1] < self.height-1 and not self.grid[cell[1]][cell[0]]["walls"][2]:
        neighbors.append((cell[0], cell[1]+1))
    return neighbors
if name == "main":
    maze = Maze(10, 10)
    maze.generate((0, 0), (9, 9))
    print(maze)
    print(maze.solve_dfs((0, 0), (9, 9)))
    print(maze.solve_bfs((0, 0), (9, 9)))
```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.
```