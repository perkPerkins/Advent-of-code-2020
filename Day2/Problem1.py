# How many passwords are valid according to their policies?

with open("input.txt", "r") as f:

    lines = f.readlines()
    valid_passwords = 0

    for line in lines:

        info = line.split()
        character_range = info[0].split("-")
        required_character = info[1].strip(":")
        password = info[2]

        character_count = 0
        for char in password:
            if char == required_character:
                character_count += 1

        if int(character_range[0]) <= character_count <= int(character_range[1]):
            valid_passwords += 1

    print(valid_passwords)
