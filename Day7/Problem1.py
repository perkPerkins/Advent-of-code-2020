# How many bag colors can eventually contain at least one shiny gold bag?


def count_bags(bag_map, visited, current_bag):
    visited.add(current_bag)
    if current_bag not in bag_map:
        return 1

    count = 1
    for bag in bag_map[current_bag]:
        if bag not in visited:
            count += count_bags(bag_map, visited, bag)

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

            for bag in rule[1:]:

                if bag[2:] not in bag_map:
                    bag_map[bag[2:]] = [rule[0]]
                else:
                    bag_map[bag[2:]].append(rule[0])

        print(count_bags(bag_map, set(), "shiny gold") - 1)


if __name__ == '__main__':
    main()
