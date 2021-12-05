from os import environ
import re
from typing import DefaultDict 


def get_coords(coord1, coord2):
    sign = 1 if coord2 > coord1 else -1
    return list(range(coord1, coord2 + sign, sign))


def check_points(covered_pos):
    overlapping_pos = list(filter(lambda x: x >= 2, covered_pos.values()))
    return len(overlapping_pos)


def add_points(line, covered_pos):
    x1,y1,x2,y2 = [int(value) for value in line]
    x_values = get_coords(x1, x2)
    y_values = get_coords(y1, y2)
    x_values *= len(y_values) if len(x_values) == 1 else 1 
    y_values *= len(x_values) if len(y_values) == 1 else 1 
    for x,y in zip(x_values, y_values):
        covered_pos[(x, y)] += 1  


def solve_part1(input_list):
    covered_pos = DefaultDict(lambda: 0)
    for line in input_list:
        if (line[0] == line[2] or line[1] == line[3]):
            add_points(line, covered_pos)
    return check_points(covered_pos)


def solve_part2(input_list):
    covered_pos = DefaultDict(lambda: 0)
    for line in input_list:
        add_points(line, covered_pos)
    return check_points(covered_pos)

    
if __name__ == "__main__":
    part = environ.get('part')
    with open('input.txt') as f:
        file_input = [re.split(" -> |,", x.strip()) for x in f.readlines()]
    if part == 'part1':
        print(solve_part1(file_input))
    else:
        print(solve_part2(file_input))