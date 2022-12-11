def rwrap(num, lim):
    return 0 if num >= lim else num


with open('../input.txt') as file:

    q = [0]
    while line := file.readline():
        q += [0, int(line[4:])] if 'addx' in line else [0]

    # Part 1
    stopat = [20, 60, 100, 140, 180, 220]

    # Part 2
    pixels, crt_pos = "", 0

    xreg, sums = 1, 0
    for i, val in enumerate(q):
        xreg += val

        if i + 1 in stopat:
            sums += (i + 1) * xreg

        pixels += '▀' if abs(crt_pos - xreg) <= 1 else ' '
        crt_pos = rwrap(crt_pos + 1, 40)

    print(f"Part 1: {sums}")
    print("Part 2: \n\n" +
          '\n'.join(' '.join(pixels[i:i + 40]) for i in range(0, len(pixels) - 1, 40)), '\n')
