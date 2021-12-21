from os import environ
import time


def length_5(matches, pattern):
    if matches[1].issubset(pattern):
        return 3
    elif pattern.issubset(matches[6]):
        return 5
    else:
        return 2


def length_6(matches, pattern):
    if matches[4].issubset(pattern):
        return 9
    elif matches[7].issubset(pattern):
        return 0
    else: 
        return 6


MAPPING = {
    2: lambda matches, patterns: 1, 
    3: lambda matches, patterns: 7, 
    4: lambda matches, patterns: 4,
    6: length_6,
    5: length_5,
    7: lambda matches, patterns: 8,
}

def find_nums(patterns):
    matches = {}
    patterns.sort(key=lambda x: list(MAPPING).index(len(x)))
    for pattern in patterns:
        number = MAPPING[len(pattern)](matches, set(pattern))
        matches[number] = set(pattern)
    return matches


def get_output(matches, outputs):
    num = ""
    pattern_to_num = {"".join(sorted(pattern)): key for key, pattern in matches.items()}
    for output in outputs: 
        num += str(pattern_to_num["".join(sorted(output))])
    return num


def solve_part2(file_input):
    nums = 0
    for patterns, output in file_input:
        matching = find_nums(patterns.split())
        nums += int(get_output(matching, output.split()))
    return nums


def solve_part1(data):
    s = [sum([int(len(pattern) in set({2,3,4,7})) for pattern in x[1].split()]) for x in data]
    return sum(s)


def parse_input(filename):
    with open(filename) as f:
        file_input = [line.strip().split("|") for line in f.readlines()]
    return file_input


def main():
    part = environ.get('part')
    start = time.time()
    file_input = parse_input('input.txt')
    if part == 'part1':
        res = solve_part1(file_input)
    else:
        res = solve_part2(file_input)
    end = time.time()
    print(res)
    print(f"Time: {round((end - start)*1000, 4)}ms")
    

if __name__ == "__main__":
    main()