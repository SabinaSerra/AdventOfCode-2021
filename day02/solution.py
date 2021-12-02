from os import environ

def solve_part1(file_input):
	accumulated_directions = {"forward": 0, "up": 0, "down": 0}
	for input_line in file_input:
		direction, value = input_line.split()
		accumulated_directions[direction] += int(value)
	depth = accumulated_directions["down"] - accumulated_directions["up"]
	return (accumulated_directions["forward"] * depth)

def solve_part2(input_list):
	horizontal, depth, aim = (0, 0, 0)
	for input_str in input_list:
		direction, value = input_str.split()
		if direction == "forward":
			horizontal += int(value)
			depth += aim*int(value)
		if direction == "up":
			aim -= int(value)
		if direction == "down":
			aim += int(value)
	return horizontal * depth

if __name__ == "__main__":
    part = environ.get('part')
    with open('input.txt') as f:
        file_input = f.readlines()
    if part == 'part1':
        print(solve_part1(file_input))
    else:
        print(solve_part2(file_input))
