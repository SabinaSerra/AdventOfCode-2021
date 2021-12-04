from os import environ
import math
BOARD_SIZE = 5

def is_marked_col(board, col):
    for y in range(BOARD_SIZE):
        if board[col + y*BOARD_SIZE] != "X":
            return False
    return True


def is_marked_row(board, row):
    for x in range(BOARD_SIZE):
        if board[row*BOARD_SIZE+x] != "X":
            return False
    return True


def is_bingo(board, new_ind):
    col = (new_ind) % (BOARD_SIZE)
    row = math.floor(new_ind / (BOARD_SIZE))
    return is_marked_col(board, col) or is_marked_row(board, row)


def get_next_bingo_board(called_numbers, boards):
    for number_ind, number in enumerate(called_numbers): 
        for board_ind, board in enumerate(boards):
            if number in board:
                ind = board.index(number) 
                board[ind] = "X"
                if is_bingo(board, ind):
                    return (board_ind, board, number_ind, number)


def solve_part1(input_list):
    called_numbers, boards = parse_input(input_list)
    _, bingo_board, _, number = get_next_bingo_board(called_numbers, boards)
    numbers = [int(x) if x != "X" else 0 for x in bingo_board]
    return sum(numbers)*int(number)


def get_last_bingo_board_rec(called_numbers, boards):
    if len(boards) > 1:
        board_ind, _, number_ind, _  = get_next_bingo_board(called_numbers, boards)
        return get_last_bingo_board_rec(called_numbers[number_ind::], boards[0:board_ind] + boards[board_ind+1::])
    else:
        _, board, _, number  = get_next_bingo_board(called_numbers, boards)
        return board, number


def solve_part2(input_list):
    called_numbers, boards = parse_input(input_list)
    bingo_board, number = get_last_bingo_board_rec(called_numbers, boards)
    numbers = [int(x) if x != "X" else 0 for x in bingo_board]
    return sum(numbers)*int(number)
    

def parse_input(input_list):
    called_numbers = input_list[0].strip().split(",")
    boards = []
    current_board = []
    for row in input_list[2::]:
        if row == "\n":
            boards.append(current_board)
            current_board = []
        else:
            current_board += row.strip().split()
    return called_numbers, boards


if __name__ == "__main__":
    part = environ.get('part')
    with open('input.txt') as f:
        file_input = f.readlines()
    if part == 'part1':
        print(solve_part1(file_input))
    else:
        print(solve_part2(file_input))