# Some basic parsing of the rules, returned in a tuple
def parse_rule(rule):
    numbers, letter = rule.split(' ')
    min_n, max_n = numbers.split('-')
    return (int(min_n), int(max_n), letter)

# Count the occurences of the specified letter, and see if it fits the rule
def check_valid(password, rule):
    num_letter = 0
    for letter in password:
        if letter == rule[2]:
            num_letter += 1
    return 1 if num_letter >= rule[0] and num_letter <= rule[1] else 0

# Put it all together
with open("input.dat", "r") as file:
    num_valid = 0
    lines = file.readlines()
    for line in lines:
        rule, password = line.split(':')
        parsed_rule = parse_rule(rule)
        num_valid += check_valid(password, parsed_rule)
    print ('Num valid: ' + str(num_valid))
