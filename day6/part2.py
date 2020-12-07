with open("input.dat") as file:
    contents = file.read()
    groups = contents.split("\n\n")

    total = 0
    # split into groups
    for group in groups:
        # split into people
        persons = group.split("\n")
        all_answered = None
        for person in persons:
            ind_answered = set()
            # find the occurences of each letter and do set intersection with previous groupmembers
            for letter in person:
                ind_answered.add(letter)
            if all_answered is None:
                all_answered = ind_answered
            else:
                all_answered = ind_answered.intersection(all_answered)
        total += len(all_answered)
    
print ("Group question sum: " + str(total))