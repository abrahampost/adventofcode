# Same as before, with a different valid checker
def parse_rule(rule):
    numbers, letter = rule.split(' ')
    min_n, max_n = numbers.split('-')
    return (int(min_n), int(max_n), letter)

# Grab the letters at those positions, and xor whether they contain the right thing or not
def check_valid(password, rule):
    first_occurence = password[rule[0] - 1] == rule[2]
    second_occurence = password[rule[1] - 1] == rule[2]
    return 1 if first_occurence != second_occurence else 0

with open("input.dat", "r") as file:
    num_valid = 0
    lines = file.readlines()
    for line in lines:
        rule, password = line.split(':')
        parsed_rule = parse_rule(rule)
        num_valid += check_valid(password.strip(), parsed_rule)
    print ('Num valid: ' + str(num_valid))
