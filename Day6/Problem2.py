# For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

with open("input.txt", "r") as f:

    line = f.readline()
    questions = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
                 "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
                 "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    q_count = 0
    people_in_group = 0

    while line:

        if line == "\n":

            for q in questions:

                if questions[q] == people_in_group:
                    q_count += 1

            questions = {key: 0 for key in questions}
            people_in_group = 0

        else:

            for char in line.strip():
                questions[char] += 1

            people_in_group += 1

        line = f.readline()

    print(q_count)
