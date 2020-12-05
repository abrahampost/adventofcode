slope = (3, 1)

with open("input.dat", "r") as file:
    lines = [x.strip() for x in file.readlines()]
    line_width = len(lines[0])

    position = (0, 0)
    trees_encountered = 0

    # Check overflow
    while position[1] + slope[1] < len(lines):
        # Move to new position
        position = (position[0] + slope[0], position[1] + slope[1])

        #Check if you have hit a tree
        if lines[position[1]][position[0] % line_width] == "#":
            trees_encountered += 1
    print("Total Trees encountered: " + str(trees_encountered))