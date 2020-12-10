# What is the highest seat ID on a boarding pass?
from math import ceil

with open("input.txt", "r") as f:

    highest_id = 0
    line = f.readline()
    while line:

        row_range = [0, 127]
        col_range = [0, 7]

        for char in line:

            if char == "F":
                row_range[1] = row_range[0] + ((row_range[1] - row_range[0]) // 2)
            elif char == "B":
                row_range[0] = row_range[0] + (ceil((row_range[1] - row_range[0]) / 2))
            elif char == "L":
                col_range[1] = col_range[0] + ((col_range[1] - col_range[0]) // 2)
            else:
                col_range[0] = col_range[0] + (ceil((col_range[1] - col_range[0]) / 2))

        seat_id = row_range[0] * 8 + col_range[0]
        highest_id = max(highest_id, seat_id)
        line = f.readline()

    print(highest_id)
