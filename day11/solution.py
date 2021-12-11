from os import environ
from functools import reduce
import time
from pprint import pprint

class Grid:
    def __init__(self, input_list):
        self.width = len(input_list[0])
        self.height = len(input_list)
        self.data = reduce(lambda a,b:a+b, input_list)
        
    def __str__(self):
        grid = ""
        for ind in range(0, len(self.data), self.width):
            grid += str(self.data[ind:ind+self.width]) + "\n"
        return grid

    def get_elem(self, row, col):
        ind = row * self.width + col
        return self.data[ind]


def add_adjecent(input_list, inds):
    if len(inds) == 0:
        return 
    row, col = inds[0]
    for row_ind in range(max(row - 1, 0), min(row+2, len(input_list))):
        for col_ind in range(max(col - 1, 0), min(col + 2, len(input_list[0]))):
            input_list[row_ind][col_ind] += 1
            if input_list[row_ind][col_ind] == 10:
                inds.append((row_ind, col_ind))
    return add_adjecent(input_list, inds[1:])


def step(input_list):
    inds = []
    for row in range(0, len(input_list)):
        for col in range(0, len(input_list[0])):
            input_list[row][col] += 1
            if input_list[row][col] == 10:
                inds.append((row, col))
    add_adjecent(input_list, inds)
    return update_flare(input_list)
    

def update_flare(input_list):
    counter = 0
    for row in range(0, len(input_list)):
        for col in range(0, len(input_list[0])):
            if input_list[row][col] >= 10:
                counter += 1
                input_list[row][col] = 0
    return counter


def solve_part1(input_list, num_steps = 5):
    counter = 0
    for i in range(num_steps):
        counter += step(input_list)
    return counter 


def solve_part2(input_list):
    return

def parse_input(filename):
    with open(filename) as f:
        file_input = [[int(x) for x in list(line.strip())] for line in f.readlines()]
    return file_input

def main():
    start = time.time()
    part = environ.get('part')
    file_input = parse_input('input.txt')
    if part == 'part1':
        pprint(solve_part1(file_input))
    else:
        print(solve_part2(file_input))
    end = time.time()
    print(f"Time: {round((end - start)*1000, 4)}ms")
    

if __name__ == "__main__":
    main()

# first 0.6819ms