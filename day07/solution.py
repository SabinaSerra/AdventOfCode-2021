from os import environ
import numpy as np
import time

def calc_cost_to_line(crab_pos, fuel_func):
    upper_bound = max(crab_pos)
    lower_bound = min(crab_pos)
    current_min = np.Inf
    for pos in range(lower_bound, upper_bound + 1):
        dist = abs(pos - crab_pos)
        fuel = sum(fuel_func(dist))
        current_min = min(fuel, current_min)
    return current_min


def solve_part1(input_list):
    fuel_func = lambda dist: dist
    return calc_cost_to_line(input_list, fuel_func)


def solve_part2(input_list):
    fuel_func = lambda dist: (1 + dist) * dist * 0.5
    return calc_cost_to_line(input_list, fuel_func)


def parse_input():
    with open('input.txt') as f:
        file_input = [x.split(",") for x in f.readlines()]
    return np.array([int(x) for x in file_input[0]])


def main():
    part = environ.get('part')
    file_input = parse_input()
    if part == 'part1':
        print(solve_part1(file_input))
    else:
        print(solve_part2(file_input))
    

if __name__ == "__main__":
    main()