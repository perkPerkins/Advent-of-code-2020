# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers);
# start by counting all the trees you would encounter for the slope right 3, down 1:

with open("input.txt", "r") as f:

    toboggan_pos = 0
    line = f.readline()
    tree_count = 0

    while line:

        line = line.strip()
        if toboggan_pos > len(line) - 1:
            toboggan_pos -= len(line)

        if line[toboggan_pos] == "#":
            tree_count += 1

        toboggan_pos += 3

        line = f.readline()

    print(tree_count)
