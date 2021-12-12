from os import environ
import time
import numpy as np


def add_adjecent(grid, inds):
    if len(inds) == 0:
        return 
    row, col = inds[0]
    for row_ind in range(max(row - 1, 0), min(row+2, grid.shape[0])):
        for col_ind in range(max(col - 1, 0), min(col + 2, grid.shape[1])):
            grid[row_ind, col_ind] += 1
            if grid[row_ind, col_ind] == 10:
                inds.append([row_ind, col_ind])
    return add_adjecent(grid, inds[1:])

def step(grid):
    grid += 1
    inds = np.argwhere(grid > 9).tolist()
    add_adjecent(grid, inds)
    flared = np.argwhere(grid > 9)
    grid[flared[:,0], flared[:, 1]] = 0
    return flared.shape[0]

def solve_part1(grid, num_steps = 100):
    counter = 0
    for i in range(num_steps):
        counter += step(grid)
    return counter 


def solve_part2(grid):
    i = 0
    while i < 1000:
        i += 1
        step(grid)
        if np.all(grid == 0):
            return i 
        

def parse_input(filename):
    with open(filename) as f:
        file_input = [[int(x) for x in list(line.strip())] for line in f.readlines()]
    return file_input

def main():
    part = environ.get('part')
    start = time.time()
    file_input = parse_input('input.txt')
    grid = np.array(file_input)
    if part == 'part1':
        res = solve_part1(grid)
    else:
        res = solve_part2(grid)
    end = time.time()
    print(res)
    print(f"Time: {round((end - start)*1000, 4)}ms")
    

if __name__ == "__main__":
    main()

# first 0.6819ms