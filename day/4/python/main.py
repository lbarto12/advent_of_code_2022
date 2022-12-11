

def full_overlap(a, b):
    return a[0] <= b[0] and a[1] >= b[1] or b[0] <= a[0] and b[1] >= a[1]


with open('../input.txt') as file:

    intersects = 0
    contains = 0

    while line := file.readline():
        e1, e2 = line.split(',')
        e1 = tuple(int(i) for i in e1.split('-'))
        e2 = tuple(int(i) for i in e2.split('-'))

        # Part 1
        if full_overlap(e1, e2):
            contains += 1

        # Part 2
        i1 = set(range(e1[0], e1[1] + 1))
        i2 = set(range(e2[0], e2[1] + 1))

        if i1.intersection(i2):
            intersects += 1

    print(f"Part 1: {contains}")
    print(f"Part 2: {intersects}")
