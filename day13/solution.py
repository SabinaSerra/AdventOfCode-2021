from os import environ
import time
FOLD_TEXT = "fold along "
FOLD_IND = 2

def fold_paper(fold, dots):
    fold = fold[len(FOLD_TEXT):]
    fold_num = int(fold[FOLD_IND:])
    if fold[0] == "x":
        folded = set((x,y) for x,y, in filter(lambda dot: dot[0]>= fold_num, dots))
        keep = set((x,y) for x,y, in filter(lambda dot: dot[0]< fold_num, dots))
        new_values = [(fold_num*2 - x, y) for x,y in folded]
    else: 
        folded = set((x,y) for x,y, in filter(lambda dot: dot[1]>= fold_num, dots))
        keep = set((x,y) for x,y, in filter(lambda dot: dot[1]< fold_num, dots))
        new_values = [(x, fold_num*2 - y) for x,y in folded]
    dots = keep.union(new_values)
    return dots

def solve_part1(folds, dots):
    dots = fold_paper(folds[0], dots)
    return len(dots)


def solve_part2(folds, dots):
    for fold in folds:
        dots = fold_paper(fold, dots)
    grid = [[" "]*40 for i in range(7)]
    for x,y in dots: 
        grid[y][x] = "#" 
    for row in grid: 
        print("".join(row))
    
        

def parse_input(filename):
    with open(filename) as f:
        file_input = f.read()
    file_input = file_input.split("\n")
    folds_inds = file_input.index("")
    folds = file_input[folds_inds+1:]
    dots = set((int(line.split(",")[0]), int(line.split(",")[1])) for line in file_input[:folds_inds])
    return folds, dots

def main():
    part = environ.get('part')
    start = time.time()
    folds, dots = parse_input('input.txt')
    if part == 'part1':
        res = solve_part1(folds, dots)
    else:
        res = solve_part2(folds, dots)
    end = time.time()
    print(res)
    print(f"Time: {round((end - start)*1000, 4)}ms")
    

if __name__ == "__main__":
    main()