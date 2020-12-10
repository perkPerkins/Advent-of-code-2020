# Count the number of valid passports - those that have all required fields.
# Treat cid as optional. In your batch file, how many passports are valid?

with open("input.txt", "r") as f:

    lines = f.readlines()
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports = 0
    passport = ""

    for line in lines:

        if line != "\n":
            passport += line.replace("\n", " ")

        else:

            passport_valid = True

            for field in required_fields:
                if field not in passport:

                    passport_valid = False
                    break

            if passport_valid:
                valid_passports += 1

            passport = ""

    print(valid_passports)
