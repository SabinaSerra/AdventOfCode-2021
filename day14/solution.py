from os import environ
import time
from collections import defaultdict


def solve_part1(polymer: str, rules: dict[str, str]):
    res = defaultdict(lambda: 0)
    for i in range(len(polymer) - 1):
        rec_sol(polymer[i:i+2], rules, res, 10)
    print(max(res.values()) - min(res.values()))


def rec_sol(polymer: str, rules: dict[str, str], res: dict[str, int], count: int):
    if count <= 0 or polymer not in rules:
        return
    new_letter = rules[polymer]
    res[new_letter] += 1
    rec_sol(polymer[0] + new_letter, rules, res, count - 1)
    rec_sol(new_letter + polymer[1], rules, res, count - 1)


def calc(letter_count: dict[str, int], curr_pairs: dict[str, int], rules: dict[str, str]):
    next_pairs = defaultdict(lambda:0)
    for rule in rules:
        if rule in curr_pairs:
            new_letter = rules[rule]
            count = curr_pairs.pop(rule)
            letter_count[new_letter] += count
            next_pairs[rule[0] + new_letter] += count
            next_pairs[new_letter + rule[1]] += count
    return next_pairs

    
def solve_part2(polymer: str, rules: dict[str: str]):
    letter_counts = defaultdict(lambda: 0)
    curr_pairs = defaultdict(lambda: 0)
    letter_counts[polymer[-1]] += 1
    for i in range(len(polymer) - 1):
        letter_counts[polymer[i]] += 1
        curr_pairs[polymer[i:i+2]] += 1
    for i in range(10):
        curr_pairs = calc(letter_counts, curr_pairs, rules)
    print(max(letter_counts.values()) - min(letter_counts.values()))

    
        

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
        res = solve_part1(polymer, rules)
    else:
        res = solve_part2(polymer, rules)
    end = time.time()
    print(res)
    print(f"Time: {round((end - start)*1000, 4)}ms")
    

if __name__ == "__main__":
    main()