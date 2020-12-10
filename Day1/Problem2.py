# What is the product of the three entries that sum to 2020?

with open("input.txt", "r") as f:

    vals = f.readlines()
    pairing = {}

    for i in vals:

        val = int(i)
        pairing[val] = 2020 - val

    sol_found = False

    for i in pairing:

        remaining_sum = pairing[i]

        for j in pairing:

            if remaining_sum - j in pairing:

                print(f"{i} + {j} + {remaining_sum - j} = {i + j + (remaining_sum - j)} and "
                      f"{i} * {j} * {remaining_sum - j} = {i * j * (remaining_sum - j)}")
                sol_found = True

            if sol_found:
                break
