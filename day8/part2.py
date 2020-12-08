answer = None

def change_one(instr, line_no):
    global answer
    # returns false if program is invalid or doesn't terminate
    instructions = instr[:]
    if instructions[line_no][0] == "jmp":
        instructions[line_no] = ("nop", instructions[line_no][1])
    elif instructions[line_no][0] == "nop":
        instructions[line_no] = ("jmp", instructions[line_no][1])
    else:
        return False
    seen = set()
    pc = 0
    accumulator = 0
    while pc < len(instructions):
        if pc in seen:
            return False
        else:
            seen.add(pc)
        op, num = instructions[pc]
        if op == "nop":
            pc += 1
            continue
        elif op == "acc":
            pc += 1
            accumulator += num
        elif op == "jmp":
            pc += num
        else:
            print("UNRECOGNIZED OP: ", op, ". Exiting...")
            exit(1)
    # saves the correct answer. could use tuple also
    answer = accumulator
    return True

with open("input.dat") as file:
    instructions = []
    for line in file.readlines():
        op, num = line.strip().split(" ")
        instructions.append((op, int(num)))

    for i in range(0, len(instructions)):
        # try switching out all the instructions one by one and running the program
        if change_one(instructions, i):
            print ("Changing instruction number: ", i, " from ", instructions[i], " stops progam with acc: ", answer)
            break
    