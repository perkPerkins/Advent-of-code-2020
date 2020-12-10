# Dynamic programming for the win!

with open("input.txt", "r") as f:
    joltages = []
    line = f.readline()

    while line:
        joltages.append(int(line))
        line = f.readline()

    joltages.sort()
    joltages.reverse()
    joltages.append(0)
    arrangements = {}

    for i in range(len(joltages)):

        if i < 3:

            if i == 0 or i == 1:
                arrangements[i] = 1

            else:

                arrangements[i] = arrangements[1]

                if joltages[0] - joltages[i] <= 3:
                    arrangements[i] += arrangements[0]

        else:

            arrangements[i] = 0
            for j in range(i - 3, i):

                if joltages[j] - joltages[i] <= 3:
                    arrangements[i] += arrangements[j]

    print(arrangements[len(joltages) - 1])
