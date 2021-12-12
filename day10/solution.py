from os import environ
import time
from queue import LifoQueue
import math

CHUNK_MAP = {
    "[": "]",
    "(": ")",
    "<": ">",
    "{": "}"
}

SCORE_MAP_PART1 = {
    "]": 57, 
    ")": 3,
    "}": 1197, 
    ">": 25137
}

SCORE_MAP_PART2 = {
    "(": 1, 
    "[": 2,
    "{": 3, 
    "<": 4
}

def find_syntax_error(line):
    open_chunks = LifoQueue()
    for char in line: 
        if char in CHUNK_MAP.keys():
            open_chunks.put(char)
        elif open_chunks.empty():
            return char
        else:
            curr_chunk = open_chunks.get()
            if char != CHUNK_MAP[curr_chunk]:
                return char
    return open_chunks

def autocomplete(queue):
    points = 0
    while not queue.empty():
        char = queue.get()
        points *= 5
        points += SCORE_MAP_PART2[char]
    return points

def solve_part1(data):
    points = 0
    for line in data:
        char = find_syntax_error(line)
        if isinstance(char, str):
            points += SCORE_MAP_PART1[char]
    return points 

def solve_part2(data):
    scores = []
    for line in data:
        res = find_syntax_error(line)
        if isinstance(res, str):
            pass
        else:
            score = autocomplete(res)
            scores.append(score)
    scores.sort()
    return scores[math.floor(len(scores)/2)] 
        

def parse_input(filename):
    with open(filename) as f:
        file_input = [line.strip() for line in f.readlines()]
    return file_input


def main():
    part = environ.get('part')
    start = time.time()
    data = parse_input('input.txt')
    if part == 'part1':
        res = solve_part1(data)
    else:
        res = solve_part2(data)
    end = time.time()
    print(res)
    print(f"Time: {round((end - start)*1000, 4)}ms")
    

if __name__ == "__main__":
    main()