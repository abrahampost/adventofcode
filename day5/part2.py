def to_binary(letters, i):
    return i.replace(letters[0], "0").replace(letters[1], "1")

with open("input.dat", "r") as file:
    highest = 0
    seats = set()
    for line in file.readlines():
        row = int(to_binary(("F", "B"), line[:7]), base=2)
        column = int(to_binary(("L", "R"), line[7:10]), base=2)
        seat_id = row * 8 + column
        seats.add(seat_id)

    # Sans the missing first and last seats, find the set of all seats and diff that with what you found
    min_seat = min(seats)
    max_seat = max(seats)
    all_seats = set(range(min_seat, max_seat))

    your_seat = all_seats.difference(seats)

    print("Your Seat Id: " + str(your_seat.pop()))