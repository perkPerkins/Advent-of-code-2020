with open("input.txt", "r") as f:
    lines = f.readlines()
    acc = 0
    visited = set()
    line_num = 0

    while line_num not in visited:

        visited.add(line_num)
        line = lines[line_num].split(" ")
        acc += int(line[1]) if line[0] == "acc" else 0
        line_num += int(line[1]) if line[0] == "jmp" else 1

    print(acc)

