# Game of Life Simulation - 3972

**Language**: `Python`

**Lines of code**: `56`

## Description

The program is written in Python and simulates the famous "Game of Life" cellular automaton developed by John Conway. The program displays the simulation in the terminal using Unicode characters.



## Code

``` Python
import os
import time

# Set the size of the grid
GRID_SIZE = (20, 20)

# Set the number of generations to simulate
NUM_GENERATIONS = 50

# Initialize the grid with zeros
grid = [[0 for y in range(GRID_SIZE[1])] for x in range(GRID_SIZE[0])]

# Set some cells to "alive" to start the simulation
grid[5][5] = 1
grid[5][6] = 1
grid[6][5] = 1
grid[6][6] = 1
grid[10][10] = 1
grid[11][10] = 1
grid[10][11] = 1
grid[11][11] = 1

# Define a function to count the number of live neighbors for a given cell
def count_live_neighbors(x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if x+i < 0 or x+i >= GRID_SIZE[0]:
                continue
            if y+j < 0 or y+j >= GRID_SIZE[1]:
                continue
            if grid[x+i][y+j] == 1:
                count += 1
    return count

# Main loop to simulate the generations
for generation in range(NUM_GENERATIONS):
    os.system('clear')
    print(f"Generation {generation}")
    for x in range(GRID_SIZE[0]):
        for y in range(GRID_SIZE[1]):
            count = count_live_neighbors(x, y)
            if grid[x][y] == 1:
                if count < 2 or count > 3:
                    grid[x][y] = 0
            else:
                if count == 3:
                    grid[x][y] = 1
            if grid[x][y] == 1:
                print("██", end="")
            else:
                print("  ", end="")
        print()
    time.sleep(0.1)

```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.

Also tell me what language it is
```