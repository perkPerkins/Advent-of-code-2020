# How many passwords are valid according to their policies?

with open("input.txt", "r") as f:

    lines = f.readlines()
    valid_passwords = 0

    for line in lines:

        info = line.split()
        character_pos = info[0].split("-")
        pos1, pos2 = int(character_pos[0]) - 1, int(character_pos[1]) - 1
        required_character = info[1].strip(":")
        password = info[2]

        if password[pos1] == required_character and password[pos2] == required_character:
            continue

        elif password[pos1] == required_character or password[pos2] == required_character:
            valid_passwords += 1

    print(valid_passwords)
