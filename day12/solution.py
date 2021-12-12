from os import environ
import time
from typing import DefaultDict
from queue import Queue


def find_paths(cave_map, part="part1"):
    queue = Queue()
    queue.put((["start"], False))
    paths = []
    while not queue.empty():
        curr_path, has_two_small_caves = queue.get()
        neighbors = cave_map[curr_path[-1]]
        for neighbor in neighbors:
            if neighbor == "end":
                paths.append(curr_path + [neighbor])
            elif (neighbor == "start"):
                pass
            elif neighbor.isupper() or not neighbor in curr_path:
                queue.put((curr_path + [neighbor], has_two_small_caves))
            elif part == "part2" and not has_two_small_caves:
                queue.put((curr_path + [neighbor], True))
    return paths

        
def convert_to_cave_map(file_input):
    cave_map = DefaultDict(lambda: set())
    for connection in file_input:
        cave_map[connection[0]].add(connection[1])
        cave_map[connection[1]].add(connection[0])
    return cave_map
    
    
def parse_input(filename):
    with open(filename) as f:
        file_input = [x.strip().split("-") for x in f.readlines()]
    return convert_to_cave_map(file_input)

def main():
    part = environ.get('part')
    start = time.time()
    file_input = parse_input('input.txt')
    if part == 'part1':
        res = len(find_paths(file_input, part))
    else:
        res = len(find_paths(file_input, "part2"))
    end = time.time()
    print(res)
    print(f"Time: {round((end - start)*1000, 4)}ms")
    

if __name__ == "__main__":
    main()
