# Same as part 1, just put it in it's own function and called it a few times

lines = []
line_width = 0
def read_lines():
    global lines
    global line_width
    with open("input.dat", "r") as file:
        lines = [x.strip() for x in file.readlines()]
        line_width = len(lines[0])


def calc_trees(slope):
    global lines
    global line_width
    position = (0, 0)
    trees_encountered = 0

    # Check overflow
    while position[1] + slope[1] < len(lines):
        # Move to new position
        position = (position[0] + slope[0], position[1] + slope[1])

        #Check if you have hit a tree
        if lines[position[1]][position[0] % line_width] == "#":
            trees_encountered += 1
    return trees_encountered

read_lines()
result = calc_trees((1,1)) * calc_trees((3,1)) * calc_trees((5,1)) * calc_trees((7,1)) * calc_trees((1,2))
print(result)