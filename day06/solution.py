from os import environ
from typing import DefaultDict 

NORMAL_SPAWN = 6
FIRST_SPAWN = 8

def shift_timers(timers):
    new_timers = DefaultDict(lambda: 0)
    new_fish = timers[0]
    for time in range(0, FIRST_SPAWN):
        new_timers[time] = timers[time+1]
    new_timers[NORMAL_SPAWN] += new_fish
    new_timers[FIRST_SPAWN] = new_fish
    return new_timers

def calc_fish(input_list, nr_days):
    timers = DefaultDict(lambda: 0)
    for timer in input_list:
        timers[timer] += 1
    for day in range(nr_days):
        timers = shift_timers(timers)      
    return sum(timers.values())


def solve_part1(input_list):
    return calc_fish(input_list, 80)


def solve_part2(input_list):
    return calc_fish(input_list, 256)


def main():
    part = environ.get('part')
    with open('input.txt') as f:
        file_input = [list(map(lambda timer: int(timer), x.strip().split(","))) for x in f.readlines()][0]
    if part == 'part1':
        print(solve_part1(file_input))
    else:
        print(solve_part2(file_input))
    

if __name__ == "__main__":
    main()