fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])

#Separate all the fields
def parse_passport(passport):
    all_entries = []
    lines = passport.split("\n")
    for line in lines:
        all_entries = all_entries + line.split(' ')
    return all_entries

# See which fields are available, and compare to the fields we are looking for
def validate_passport(passport_fields):
    found_fields = set()
    for field in passport_fields:
        f, _ = field.split(':')
        found_fields.add(f)

    diff = fields.difference(found_fields)
    if len(diff) == 0 or len(diff) == 1 and "cid" in diff:
        return 1
    return 0

# Put it all together
with open("input.dat", "r") as file:
    content = file.read()
    #an empty line is just two line breaks in a row
    passports = content.split("\n\n")
    
    total_valid = 0
    for passport in passports:
        total_valid += validate_passport(parse_passport(passport))
    print("Total valid: " + str(total_valid))