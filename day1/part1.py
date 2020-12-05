TARGET = 2020

# Adds seen numbers to set.
# If the diff between the target and current num is in set, that is the pair
with open("input.dat", "r") as file:
    seen = set()
    for line in file.readlines():
        num = int(line)
        diff = TARGET - num
        if diff in seen:
            print(num * diff)
            break
        else:
            seen.add(num)