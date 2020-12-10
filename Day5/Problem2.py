# What is the highest seat ID on a boarding pass?
from math import ceil

with open("input.txt", "r") as f:

    line = f.readline()
    seats = []

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

        seats.append(row_range[0] * 8 + col_range[0])
        line = f.readline()

    seats.sort()
    prev_seat = seats[0]

    for seat in seats[1:]:

        if seat - prev_seat == 2:
            print(seat - 1)
        prev_seat = seat
    print(seats)
