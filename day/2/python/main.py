
# Values of Rock, Paper and Scissors
vals = {
    "A": 1, "X": 1,
    "B": 2, "Y": 2,
    "C": 3, "Z": 3
}

# Retrieve the score of the match
get_result = {
    "A": {"Z": 0, "X": 3, "Y": 6},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"Y": 0, "Z": 3, "X": 6}
}

# Determine recommended action (Part 2)
actions = {
    "X": {"A": "Z", "B": "X", "C": "Y"},
    "Y": {"A": "X", "B": "Y", "C": "Z"},
    "Z": {"A": "Y", "B": "Z", "C": "X"}
}

with open("../input.txt") as file:

    part_1_sum = part_2_sum = 0

    while match := file.readline():
        opponent, me = match.strip().split(" ")

        # Part 1
        part_1_sum += vals[me] + get_result[opponent][me]

        # Part 2
        p2_action = actions[me][opponent]
        part_2_sum += vals[p2_action] + get_result[opponent][p2_action]

    print("Part 1:", part_1_sum)
    print("Part 2:", part_2_sum)
