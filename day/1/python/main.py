

with open('../input.txt') as file:
    sums = list(sorted([sum(int(j) for j in i.split("\n")) for i in file.read().split('\n\n')]))

    print(f'Part 1: {sums[-1]}')
    print(f'Part 2: {sum(sums[-3:])}')