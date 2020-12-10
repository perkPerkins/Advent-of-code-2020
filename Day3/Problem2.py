# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

with open("input.txt", "r") as f:

    line = f.readline()
    current_line = 0
    toboggan_positions = [0, 0, 0, 0, 0]
    delta_x = [1, 3, 5, 7, 1]
    delta_y = [1, 1, 1, 1, 2]
    tree_counts = [0, 0, 0, 0, 0]

    while line:

        line = line.strip()

        for i in range(len(toboggan_positions)):

            if toboggan_positions[i] > len(line) - 1:

                toboggan_positions[i] -= len(line)

            if current_line % 2 == 0:

                if line[toboggan_positions[i]] == "#":

                    tree_counts[i] += 1

                toboggan_positions[i] += delta_x[i]

            elif delta_y[i] == 1:

                if line[toboggan_positions[i]] == "#":

                    tree_counts[i] += 1

                toboggan_positions[i] += delta_x[i]

        line = f.readline()
        current_line += 1

    solution = 1
    for count in tree_counts:
        solution *= count

    print(solution)

