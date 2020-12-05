# These are just binary numbers

def to_binary(letters, i):
    return i.replace(letters[0], "0").replace(letters[1], "1")

with open("input.dat", "r") as file:
    highest = 0
    for line in file.readlines():
        row = int(to_binary(("F", "B"), line[:7]), base=2)
        column = int(to_binary(("L", "R"), line[7:10]), base=2)
        seat_id = row * 8 + column
        highest = max(highest, seat_id)
    
    print("Highest Seat Id: " + str(highest))