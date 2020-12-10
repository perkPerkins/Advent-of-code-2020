with open("input.txt", "r") as f:
    invalid_num = 36845998
    contiguous_set = []
    current_sum = 0
    lines = f.readlines()

    for i in range(len(lines)):

        contiguous_set.append(int(lines[i]))
        current_sum += int(lines[i])

        for j in range(i + 1, len(lines)):

            contiguous_set.append(int(lines[j]))
            current_sum += int(lines[j])
            if current_sum >= invalid_num:
                break

        if current_sum > invalid_num:
            contiguous_set.clear()
            current_sum = 0

        else:
            print(min(contiguous_set) + max(contiguous_set))
            break
