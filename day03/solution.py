from os import environ

def transpose_input(input_list):
    transposed = []
    for i in range(len(input_list[0])):
        transposed.append([int(row[i]) for row in input_list])
    return transposed


def solve_part1(input_list):
    tot_size = len(input_list)
    transposed = transpose_input(input_list)
    counts = [int(sum(row) > tot_size/2) for row in transposed]
    epsilon = [str(int(not value)) for value in counts]
    gamma = [str(value) for value in counts]
    return int("".join(epsilon), 2)*int("".join(gamma), 2)


def filter_bits(ind, substring, input_list, measurement_func):
    list_size = len(input_list)
    if list_size == 1:
        return input_list
    else:
        current_elems = [int(row[ind]) for row in input_list]
        bit = measurement_func(current_elems, list_size)
        substring += bit
        filtered_input = list(filter((lambda x: str(x[0:len(substring)]) == substring), input_list))
        return filter_bits(ind + 1, substring, filtered_input, measurement_func)


def get_measuremet(input_list, measurement_func):
    measurement = filter_bits(0, "", input_list, measurement_func)
    return int("".join(measurement[0]), 2)


def solve_part2(input_list):
    oxygen_func = lambda bit_list, list_size: str(int(sum(bit_list) < list_size/2))
    co2_func = lambda bit_list, list_size: str(int(sum(bit_list) >= list_size/2))
    oxygen_measurement = get_measuremet(input_list, oxygen_func)
    co2_measurement = get_measuremet(input_list, co2_func)
    return co2_measurement * oxygen_measurement


def main():
    part = environ.get('part')
    with open('input.txt') as f:
        file_input = [x.strip() for x in f.readlines()]
    if part == 'part1':
        print(solve_part1(file_input))
    else:
        print(solve_part2(file_input))
    

if __name__ == "__main__":
    main()