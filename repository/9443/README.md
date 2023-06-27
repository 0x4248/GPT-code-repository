# Maze Solver - 9443

**Language**: `Python`

**Lines of code**: `76`

## Description

This program generates a random maze using a recursive backtracking algorithm. It then attempts to solve the maze by finding a path from the start position (top-left corner) to the end position (bottom-right corner). The solved maze is printed with the path marked by spaces. The program demonstrates maze generation and solving techniques using recursion and backtracking.

## Code

``` Python
import random

class MazeSolver:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[True] * width for _ in range(height)]

    def generate_maze(self, start_x, start_y):
        stack = [(start_x, start_y)]
        while stack:
            x, y = stack[-1]
            self.maze[y][x] = False
            neighbors = self.get_unvisited_neighbors(x, y)
            if neighbors:
                nx, ny = random.choice(neighbors)
                self.remove_wall(x, y, nx, ny)
                stack.append((nx, ny))
            else:
                stack.pop()

    def get_unvisited_neighbors(self, x, y):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx]:
                neighbors.append((nx, ny))
        return neighbors

    def remove_wall(self, x1, y1, x2, y2):
        dx, dy = x2 - x1, y2 - y1
        self.maze[y1 + dy // 2][x1 + dx // 2] = False

    def solve_maze(self, x, y, path=[]):
        if x < 0 or x >= self.width or y < 0 or y >= self.height or not self.maze[y][x]:
            return False
        if x == self.width - 1 and y == self.height - 1:
            return True
        if (x, y) in path:
            return False

        path.append((x, y))

        if self.solve_maze(x + 1, y, path):
            return True
        if self.solve_maze(x - 1, y, path):
            return True
        if self.solve_maze(x, y + 1, path):
            return True
        if self.solve_maze(x, y - 1, path):
            return True

        path.pop()
        return False

    def print_maze(self):
        for row in self.maze:
            for cell in row:
                if cell:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

# Main program
maze_solver = MazeSolver(10, 10)
maze_solver.generate_maze(0, 0)
maze_solver.print_maze()

print("Solving maze...")
if maze_solver.solve_maze(0, 0):
    print("Path found!")
    maze_solver.print_maze()
else:
    print("No path found.")

```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.
```