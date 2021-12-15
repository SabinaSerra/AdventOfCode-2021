from os import environ
from queue import PriorityQueue
import time
import math

class Node:
    def __init__(self, node_cost):
        self.node_cost = node_cost
        self.path_cost = math.inf
        self.parent = None

    def __str__(self):
        return str(self.cost)

    def __repr__(self):
        return str(self.node_cost)


def get_path(start, end, data):
    curr_ind = end
    path = []
    while curr_ind != start:
        curr_node = data[curr_ind[0]][curr_ind[1]]
        path = [curr_node] + path
        curr_ind = curr_node.parent
    return path


def find_path(data):
    queue = PriorityQueue()
    curr_node = (0, 0)
    data[0][0].path_cost = 0
    max_width = len(data[0]) - 1 
    max_height = len(data) - 1
    while curr_node != (max_height, max_width):
        y, x = curr_node
        inds = [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]
        neighbors_inds = list(filter(lambda ind: 0 <= ind[1] <= max_width and 0 <= ind[0] <= max_height, inds))
        for neighbor_ind in neighbors_inds:
            neighbor = data[neighbor_ind[0]][neighbor_ind[1]]
            cost = data[y][x].path_cost + neighbor.node_cost
            if cost < neighbor.path_cost:
                neighbor.path_cost = cost
                neighbor.parent = curr_node
                queue.put((neighbor.path_cost, neighbor_ind))
        curr_node = queue.get()[1]
    return data[curr_node[0]][curr_node[1]].path_cost
    

def solve_part1(data):
    cost = find_path(data)
    return cost

def update_cost(old, increase):
    new_value = old + increase
    if new_value > 9:
        return new_value - 9
    return new_value

def get_new_data(data):
    new_data = []
    for row in range(len(data)):
        new_col = []
        for i in range(0, 5):
            new_col += [Node(update_cost(elem.node_cost, i)) for elem in data[row]]
        new_data.append(new_col)
    added_rows = []
    for i in range(1, 5):
        for row in range(len(new_data)):
            added_rows.append([Node(update_cost(elem.node_cost, i)) for elem in new_data[row]])
    return new_data + added_rows


def solve_part2(data):
    new_data = get_new_data(data)
    cost = find_path(new_data)
    return cost
    
        
def parse_input(filename):
    with open(filename) as f:
        file_input = [[Node(int(x)) for x in list(line.strip())] for line in f.readlines()]
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