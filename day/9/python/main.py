from math import copysign

directions = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


def unpack_line(ln):
    return directions[ln[0]], int(ln[2:])


def is_taut(c1, c2):
    return any(abs(c1[i] - c2[i]) > 1 for i in range(2))


def move_toward(c1, c2):
    x, y = c1[0] - c2[0], c1[1] - c2[1]
    return int(copysign(1, x)) if x else 0, int(copysign(1, y)) if y else 0


def merge_tuples(*tuples):
    return tuple(sum(i) for i in zip(*tuples))


class Rope:
    def __init__(self, length):
        self.segments = [(0, 0)] * length
        self.tail_visited = set()

    def move(self, mv):
        direction, iterations = mv

        for _ in range(iterations):
            self.segments[0] = merge_tuples(self.segments[0], direction)

            for i in range(1, len(self.segments)):
                s1 = self.segments[i - 1]
                s2 = self.segments[i]

                if is_taut(s1, s2):
                    s2 = merge_tuples(s2, move_toward(s1, s2))
                    self.segments[i] = s2

            self.tail_visited.add(self.segments[-1])


with open('../input.txt') as file:
    rope_1 = Rope(2)
    rope_2 = Rope(10)

    while line := file.readline():
        move = unpack_line(line)
        rope_1.move(move)
        rope_2.move(move)

    print("Part 1:", len(rope_1.tail_visited))
    print("Part 2:", len(rope_2.tail_visited))
