with open("input.dat") as file:
    contents = file.read()
    groups = contents.split("\n\n")

    total = 0
    for group in groups:
        # Remove duplicates, so throw it in a set
        questions = set()
        # Newlines don't matter, it's all about the group answers as a whole, so remove them
        for letter in group.replace("\n", ""):
            questions.add(letter)
        total += len(questions)
print ("Group question sum: " + str(total))