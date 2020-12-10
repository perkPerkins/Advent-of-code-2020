

def run_new_command(command_lines, line_to_change):
    line_number, accumulator = 0, 0
    lines_visited = set()

    while line_number < len(command_lines) :

        curr_line = command_lines[line_number].split(" ")
        if line_number == line_to_change:
            new_command = "jmp" if curr_line[0] == "nop" else "nop"
            curr_line = f"{new_command} {curr_line[1]}"
            
        if line_number in lines_visited:
            return None

        lines_visited.add(line_number)
        accumulator += int(curr_line[1]) if curr_line[0] == "acc" else 0
        line_number += int(curr_line[1]) if curr_line[0] == "jmp" else 1

    return accumulator


with open("input.txt", "r") as f:
    lines = f.readlines()
    acc = 0
    visited = set()
    line_num = 0
    changed_line = 0

    while lines[line_num] != "\n":

        line = lines[line_num].split(" ")

        if line_num in visited:

            solution = run_new_command(lines.copy(), line_num)
            if solution:
                break

        if line[0] != "acc":
            visited.add(line_num)

        acc += int(line[1]) if line[0] == "acc" else 0
        line_num += int(line[1]) if line[0] == "jmp" else 1

    print(f"accumulator: {solution}, line: {line_num}")

