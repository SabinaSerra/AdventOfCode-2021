from os import environ
import time
from collections import defaultdict


def calc_new_elements(element_counts: dict[str, int], curr_pairs: dict[str, int], rules: dict[str, str]):
    next_pairs = defaultdict(lambda:0)
    for rule in rules:
        if rule in curr_pairs:
            new_letter = rules[rule]
            count = curr_pairs.pop(rule)
            element_counts[new_letter] += count
            next_pairs[rule[0] + new_letter] += count
            next_pairs[new_letter + rule[1]] += count
    return next_pairs

    
def solve_parts(polymer: str, rules: dict[str: str], steps):
    element_counts = defaultdict(lambda: 0)
    curr_pairs = defaultdict(lambda: 0)
    element_counts[polymer[-1]] += 1
    for i in range(len(polymer) - 1):
        element_counts[polymer[i]] += 1
        curr_pairs[polymer[i:i+2]] += 1
    for i in range(steps):
        curr_pairs = calc_new_elements(element_counts, curr_pairs, rules)
    print(max(element_counts.values()) - min(element_counts.values()))
  

def parse_input(filename: str):
    with open(filename) as f:
        file_input = f.readlines()
    start = file_input[0].strip()
    rules = [row.strip().split(" -> ") for row in file_input[2:]]
    rules = {rule[0]: rule[1] for rule in rules}
    return start, rules


def main():
    part = environ.get('part')
    start = time.time()
    polymer, rules = parse_input('input.txt')
    if part == 'part1':
        res = solve_parts(polymer, rules, 10)
    else:
        res = solve_parts(polymer, rules, 40)
    end = time.time()
    print(res)
    print(f"Time: {round((end - start)*1000, 4)}ms")
    

if __name__ == "__main__":
    main()