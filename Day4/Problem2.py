# Your job is to count the passports where all required fields are both present and valid according to the above rules.

with open("input.txt", "r") as f:

    lines = f.readlines()
    passport_fields = {"byr": None, "iyr": None, "eyr": None, "hgt": None, "hcl": None, "ecl": None, "pid": None}
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    valid_passports = 0
    passport = ""

    for line in lines:

        if line != "\n":
            passport += line.replace("\n", " ")

        else:

            fields = passport.split()

            for field in fields:
                key, val = field.split(":")
                passport_fields[key] = val

            if None not in passport_fields.values():

                rules_met = True
                if not 1920 <= int(passport_fields["byr"]) <= 2002 or \
                        not 2010 <= int(passport_fields["iyr"]) <= 2020 or \
                        not 2020 <= int(passport_fields["eyr"]) <= 2030:
                    rules_met = False

                if "in" in passport_fields["hgt"] or "cm" in passport_fields["hgt"]:

                    if passport_fields["hgt"][-2:] == "cm" and not 150 <= int(passport_fields["hgt"][:-2]) <= 193:
                        rules_met = False

                    elif passport_fields["hgt"][-2:] == "in" and not 59 <= int(passport_fields["hgt"][:-2]) <= 76:
                        rules_met = False
                else:
                    rules_met = False

                if passport_fields["hcl"][:1] != "#":
                    rules_met = False

                for char in passport_fields["hcl"][1:]:

                    if not char.isdigit() and not 97 <= ord(char) <= 102:
                        rules_met = False

                if passport_fields["ecl"] not in eye_colors:
                    rules_met = False

                if len(passport_fields["pid"]) != 9 or not passport_fields["pid"].isdigit():
                    rules_met = False

                if rules_met:
                    valid_passports += 1

            passport = ""
            passport_fields = {"byr": None, "iyr": None, "eyr": None, "hgt": None, "hcl": None, "ecl": None,
                               "pid": None}

    print(valid_passports)
