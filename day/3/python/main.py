from string import ascii_lowercase, ascii_uppercase

# Create priority dict
# assign each ascii letter a priority of 1-52
priority = {
    char: i + 1 for i, char in enumerate(
        ascii_lowercase + ascii_uppercase
    )
}

# Part 1
with open('../input.txt') as file:
    part_1_sum = 0

    while line := file.readline():
        middle = int(len(line) / 2)
        r1, r2 = set(line[:middle]), set(line[middle:-1])
        part_1_sum += priority[r1.intersection(r2).pop()]

    print("Part 1:", part_1_sum)


# Part 2
with open('../input.txt') as file:
    part_2_sum = 0

    # Stops when first set is empty, denoting end of file
    while (lines := [set(file.readline()[:-1]) for _ in range(3)])[0]:
        part_2_sum += priority[lines[0].intersection(lines[1], lines[2]).pop()]

    print("Part 2:", part_2_sum)
