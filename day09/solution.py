from os import environ


def solve_part1(input_list):
    return


def solve_part2(input_list):
    return


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