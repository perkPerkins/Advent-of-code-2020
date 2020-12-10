with open("input.txt", "r") as f:
    last_25 = {}
    line = f.readline().strip()
    index = 0
    remove_index = 0

    while line:

        if index >= 25:

            pair_found = False

            for key in last_25.keys():

                if str(int(line) - int(key)) in last_25:
                    pair_found = True
                    break

            if not pair_found:
                print(line)
                break

            for k, v in last_25.items():
                if v == remove_index:
                    last_25.pop(k)
                    break

            remove_index += 1

        last_25[line] = index
        index += 1
        line = f.readline().strip()

