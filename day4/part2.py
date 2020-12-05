import re

fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])

#Separate all the fields
def parse_passport(passport):
    all_entries = []
    lines = passport.split("\n")
    for line in lines:
        all_entries = all_entries + line.split(' ')
    return all_entries

def validate_field(field, value):
    if field == "byr":
        return int(value) >= 1920 and int(value) <= 2002
    elif field == "iyr":
        return int(value) >= 2010 and int(value) <= 2020
    elif field == "eyr":
        return int(value) >= 2020 and int(value) <= 2030
    elif field == "hgt":
        units = value[len(value) - 2:]
        trimmed_val = int(value[:len(value) - 2])
        if units == "cm":
            return trimmed_val >= 150 and trimmed_val <= 193
        elif units == "in":
            return trimmed_val >= 59 and trimmed_val <= 76
        else:
            raise Exception("fail")
    elif field == "hcl":
        return re.fullmatch("#[0-9a-f]{6}", value) != None
    elif field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field == "pid":
        return len(value) == 9 and value.isnumeric()
    elif field == "cid":
        return True
    else:
        return False

# See which fields are available, and compare to the fields we are looking for
def validate_passport(passport_fields):
    found_fields = set()
    for field in passport_fields:
        f, value = field.split(':')
        try:
            if not validate_field(f, value):
                return 0
        except:
            return 0
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