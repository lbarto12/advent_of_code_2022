import re

with open('../input.txt') as file:

    read_stacks = []

    while line := file.readline()[:-1]:
        read_stacks.append(''.join(line[i] for i in range(1, len(line), 4)))
    read_stacks.pop()

    p1_stacks = [[row[i] for row in read_stacks if row[i] != " "][::-1] for i in range(9)]
    p2_stacks = [i[:] for i in p1_stacks]

    while line := file.readline():
        instr = tuple(int(i) for i in re.findall(r'\d+', line))

        [p1_stacks[instr[2] - 1].append(p1_stacks[instr[1] - 1].pop()) for _ in range(instr[0])]
        p2_stacks[instr[2] - 1] += [p2_stacks[instr[1] - 1].pop() for _ in range(instr[0])][::-1]

    print("Part 1: ", *[f'{stack.pop()}' for stack in p1_stacks], sep="")
    print("Part 2: ", *[f'{stack.pop()}' for stack in p2_stacks], sep="")
