import numpy as np
import time


def randomGrid(N):
    """Returns a grid of NxN random values"""
    return np.random.choice([1, 0], N * N, p=[0.2, 0.8]).reshape(N, N)


def update(grid, N):
    """Updates the grid according to Conway's rules"""
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]))

            # Apply Conway rules
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    return newGrid


def display(grid, N):
    """Displays the grid in the console"""
    print("\033[H", end="") 
    for i in range(N):
        for j in range(N):
            print('#' if grid[i, j] == 1 else ' ', end='')
        print()
    print()


def main():
    grid = randomGrid(20)

    # Run the simulation indefinetly
    while True:
        display(grid, 20)
        grid = update(grid, 20)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
