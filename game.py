import argparse
import numpy as np
import time
import os


def randomGrid(N):
    """Returns a grid of NxN random values"""
    return np.random.choice([1, 0], N * N, p=[0.2, 0.8]).reshape(N, N)


def addGlider(i, j, grid):
    """Adds a glider with top left cell at (i, j)"""
    glider = np.array([[0, 0, 1],
                       [1, 0, 1],
                       [0, 1, 1]])
    grid[i:i + 3, j:j + 3] = glider

def update(grid, N):
    """Updates the grid according to Conway's rules"""
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Compute 8-neighbor sum with toroidal boundary conditions
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]))

            # Apply Conway's rules
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    return newGrid


def display(grid, N):
    """Affiche la grille dans la console."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(N):
        for j in range(N):
            print('#' if grid[i, j] == 1 else ' ', end='')
        print()
    print()


# main() function
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation in the console.")
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    args = parser.parse_args()

    # Set grid size
    N = 20
    if args.N and int(args.N) > 8:
        N = int(args.N)

    # Set update interval
    updateInterval = 0.5
    if args.interval:
        updateInterval = float(args.interval)

    # Declare grid
    grid = np.array([])

    # Check if "glider" demo flag is specified
    if args.glider:
        grid = np.zeros(N * N).reshape(N, N)
        addGlider(1, 1, grid)
    else:  # Populate grid with random on/off values
        grid = randomGrid(N)

    # Run the simulation
    while True:
        display(grid, N)
        grid = update(grid, N)
        time.sleep(updateInterval)


# Call main
if __name__ == '__main__':
    main()