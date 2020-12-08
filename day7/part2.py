TARGET = "shiny gold"

def parse_contains(contains):
    contains_bags = []
    if contains.startswith("no"):
        return contains_bags
    else:
        others = contains.strip().split(",")
        for other in others:
            num, adj, color, _ = other.strip().split(" ")
            contains_bags.append((adj + " " + color, int(num)))
        return contains_bags

def open_bag(bags, color):
    if len(bags[color]) == 0:
        # base case bag contains no other bags
        return 0
    result = 0
    for bag in bags[color]:
        # open bags, and add the number of bags they contain, as well as how many of that bag you have to total
        result += bag[1] * open_bag(bags, bag[0]) + bag[1]
    return result

with open("input.dat") as file:
    bags = {}   
    for line in file.readlines():
        bag_type, contains = line.split(" bags contain ")
        bag_type = bag_type.strip()
        contains = contains.strip()
        bags[bag_type] = parse_contains(contains)
    
    print(TARGET, " can contain: " + str(open_bag(bags, TARGET)) + " bags")