with open("input.dat") as file:
    instructions = []
    for line in file.readlines():
        op, num = line.strip().split(" ")
        instructions.append((op, int(num)))

    seen = set()
    pc = 0
    accumulator = 0
    while pc < len(instructions):
        if pc in seen:
            print("Final accumulator is: " , accumulator)
            break
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