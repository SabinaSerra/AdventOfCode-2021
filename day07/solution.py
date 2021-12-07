from os import environ
import numpy as np
import math
import time


def calc_fuel(crab_pos, curr_pos):
    dist = abs(curr_pos - crab_pos)
    return sum((1 + dist) * dist * 0.5)


def search_pos(crab_pos, pos):
    if len(pos) == 2:
        return calc_fuel(crab_pos, pos[0])
    curr_ind = math.floor(len(pos) / 2)
    fuel1 = calc_fuel(crab_pos, pos[curr_ind - 1])
    fuel2 = calc_fuel(crab_pos, pos[curr_ind])
    if fuel1 < fuel2:
        return search_pos(crab_pos, pos[0:curr_ind])
    else:
        return search_pos(crab_pos, pos[curr_ind:])
    

def calc_cost_to_line(crab_pos):
    upper_bound = max(crab_pos)
    lower_bound = min(crab_pos)
    pos = list(range(lower_bound, upper_bound + 1))
    return search_pos(np.array(crab_pos), pos)


def solve_part1(input_list):
    input_list.sort()
    median = input_list[math.ceil(len(input_list)/2)]
    fuel = sum(abs(median - np.array(input_list)))
    return fuel


def calc_cost_to_line1(crab_pos, fuel_func):
    upper_bound = max(crab_pos)
    lower_bound = min(crab_pos)
    current_min = np.Inf
    for pos in range(lower_bound, upper_bound + 1):
        dist = abs(pos - crab_pos)
        fuel = sum(fuel_func(dist))
        current_min = min(fuel, current_min)
    return current_min


def solve_part2(input_list):
    return calc_cost_to_line(input_list) 


def parse_input():
    with open('input.txt') as f:
        file_input = [x.split(",") for x in f.readlines()]
    return [int(x) for x in file_input[0]]


def main():
    part = environ.get('part')
    file_input = parse_input()
    if part == 'part1':
        print(solve_part1(file_input))
    else:
        print(solve_part2(file_input))
    

if __name__ == "__main__":
    main()