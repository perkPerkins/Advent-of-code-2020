# You need to find the two entries that sum to 2020 and then multiply those two numbers together.

with open("input.txt", "r") as f:

    vals = f.readlines()
    pairing = {}

    for i in vals:

        val = int(i)
        pairing[val] = 2020 - val

    for i in pairing:

        if pairing[i] in pairing:

            sol = i + pairing[i]
            print(f"{i} + {pairing[i]} = {i + pairing[i]} and {i} * {pairing[i]} = {i * pairing[i]}")
            break
