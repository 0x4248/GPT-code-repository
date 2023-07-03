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