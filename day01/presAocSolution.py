import math
from os import environ

def is_prime(num):
    return not any([(num % i == 0) for i in range(2, math.floor(math.sqrt(num)) + 1)])


def solve_part1(input_list):
    sum = 0
    for idx, val in enumerate(input_list):
        if is_prime(val):
            sum += idx*val
    return sum


def solve_part2(input_list):
    subtract = filter(lambda x: not is_prime(x), input_list[1::2])
    add = filter(lambda x: not is_prime(x), input_list[::2])
    return sum(add) - sum(subtract)

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