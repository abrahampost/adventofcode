def parse_contains(contains):
    contains_bags = []
    if contains.startswith("no"):
        return contains_bags
    else:
        others = contains.strip().split(",")
        for other in others:
            num, adj, color, _ = other.strip().split(" ")
            contains_bags.append((adj + " " + color, num))
        return contains_bags

def open_bag(bags, color):
    if color == "shiny gold":
        return True
    for bag in bags[color]:
        result = open_bag(bags, bag[0])
        if result:
            return True
    
    return False

with open("input.dat") as file:
    bags = {}   
    for line in file.readlines():
        bag_type, contains = line.split(" bags contain ")
        bag_type = bag_type.strip()
        contains = contains.strip()
        bags[bag_type] = parse_contains(contains)
    

    num_containers = 0

    for bag_color, _ in bags.items():
        if bag_color == "shiny gold":
            continue
        num_containers += 1 if open_bag(bags, bag_color) else 0
    
    print(str(num_containers) + " can contains shiny gold bags")