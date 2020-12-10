with open("input.txt", "r") as f:
    joltages = []
    line = f.readline()

    while line:
        joltages.append(int(line))
        line = f.readline()

    one_jolt_diffs, three_jolt_diffs, joltage = 0, 0, 0
    joltages.sort()

    for jolt in joltages:
        one_jolt_diffs += 1 if jolt - joltage == 1 else 0
        three_jolt_diffs += 1 if jolt - joltage == 3 else 0
        joltage = jolt

    three_jolt_diffs += 1
    print(one_jolt_diffs * three_jolt_diffs)