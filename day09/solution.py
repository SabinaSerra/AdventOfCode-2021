from os import environ
import numpy as np
import time


def calc_low_points(shifted: np.ndarray, org: np.ndarray, res: np.ndarray) -> np.ndarray:
    curr_res = (shifted - org) > 0
    return np.logical_and(res, curr_res)


def find_low_points(input_list: np.ndarray) -> np.ndarray:
    up = np.delete(input_list, 0, axis=0)
    up = np.pad(up, ((0,1),(0,0)), 'constant', constant_values = 10)
    res = np.ones(input_list.shape)
    res = calc_low_points(up, input_list, res)
    down = np.delete(input_list, -1, axis=0)
    down = np.pad(down, ((1,0),(0,0)), 'constant', constant_values = 10)
    res = calc_low_points(down, input_list, res)
    left = np.delete(input_list, 0, axis=1)
    left = np.pad(left, ((0,0),(0,1)), 'constant', constant_values = 10)
    res = calc_low_points(left, input_list, res)
    right = np.delete(input_list, -1, axis=1)
    right = np.pad(right, ((0,0),(1,0)), 'constant', constant_values = 10)
    res = calc_low_points(right, input_list, res)
    return res

def solve_part1(input_list: np.ndarray) -> np.ndarray:
    res = find_low_points(input_list)
    num_lowpoints = np.sum(res)
    res = res*input_list
    return num_lowpoints + np.sum(res)


def count_bazin(last_height: int, ind: tuple[int, int], input_list: np.ndarray) -> int:
    is_in_range = (0 <= ind[0] < input_list.shape[0]) and (0 <= ind[1] < input_list.shape[1])
    if not is_in_range:
        return 0
    curr_height = input_list[ind]
    if (curr_height == 9) or (curr_height <= last_height):
        return 0
    input_list[ind] = -1
    return 1 + count_bazin(curr_height, (ind[0]-1, ind[1]), input_list) + \
            count_bazin(curr_height, (ind[0]+1, ind[1]), input_list) + \
            count_bazin(curr_height, (ind[0], ind[1]-1), input_list) + \
            count_bazin(curr_height, (ind[0], ind[1]+1), input_list)
    

def solve_part2(input_list: np.ndarray) -> int:
    low_points = find_low_points(input_list)
    inds = np.where(low_points > 0)
    bazin_counts = []
    for i in range(inds[0].shape[0]):
        mutable_input = np.copy(input_list)
        bazin_counts += [count_bazin(-1, (inds[0][i], inds[1][i]), mutable_input)]
    bazin_counts.sort()
    return bazin_counts[-3]*bazin_counts[-2]*bazin_counts[-1]

def convert_to_int(input_list: list[str]) -> list[int]:
    return [int(x) for x in input_list]

def main():
    part = environ.get('part')
    start = time.time()
    with open('input.txt') as f:
        file_input = [list(row.strip()) for row in f.readlines()]
    file_input = np.array([convert_to_int(row) for row in file_input])
    if part == 'part1':
        res = solve_part1(file_input)
    else:
        res = solve_part2(file_input)
    end = time.time()
    print(res)
    print(f"Time: {round((end - start)*1000, 4)}ms")
    

if __name__ == "__main__":
    main()