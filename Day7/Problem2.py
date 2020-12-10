# How many individual bags are required inside your single shiny gold bag?


def count_bags(bag_map, current_bag):
    if current_bag[1] not in bag_map:
        return int(current_bag[0])

    count = int(current_bag[0])
    for bag in bag_map[current_bag[1]]:
        count += int(current_bag[0]) * count_bags(bag_map, bag)

    return count


def main():
    with open("input.txt", "r") as f:
        line = f.readline()
        bag_rules = []
        while line:
            bag_rule = line.replace("bags contain", ",").replace("bags", "").replace("bag", "").replace(".", "")
            bag_rules.append([bag.rstrip().lstrip() for bag in [rule for rule in bag_rule.replace(".", "").split(",")]])
            line = f.readline()

        bag_map = {}
        for rule in bag_rules:

            if rule[1] != "no other":
                bag_map[rule[0]] = []

                for bag in rule[1:]:
                    bag_map[rule[0]].append((bag[:1], bag[2:]))

        print(count_bags(bag_map, (1, "shiny gold")) - 1)


if __name__ == '__main__':
    main()
