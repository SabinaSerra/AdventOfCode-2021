import math
from os import environ


def solve_part1(input_list):
    result = [input_list[i-1] < input_list[i] for i in range(1, len(input_list))]
    return sum(result)


def solve_part2(input_list):
    sums = [input_list[i-2] + input_list[i-1] + input_list[i] for i in range(2, len(input_list))]
    return solve_part1(sums)


def main():
    part = environ.get('part')
    with open('input.txt') as f:
        file_input = [int(x) for x in f.readlines()]
    if part == 'part1':
        print(solve_part1(file_input))
    else:
        print(solve_part2(file_input))
    

if __name__ == "__main__":
    main()