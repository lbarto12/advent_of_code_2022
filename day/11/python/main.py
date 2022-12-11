import re
import math


class Monkey:
    MONKEYS = []
    TOTAL_MONKEYS = 0

    @staticmethod
    def operation(num1, op, num2):
        return int(num1) ** 2 if num2 == 'old' else {'+': num1 + num2, '*': num1 * num2}[op]

    def __init__(self, attributes):

        _, items, op, test, true, false = attributes

        self.items = list(map(int, re.findall(r'\d+', items)))
        op = re.search(r'old (.) (.*)$', op)
        self.op = (op[1], int(op[2]) if op[2].isdigit() else op[2])
        self.test = int(re.search(r'by (\d+)$', test)[1])
        self.true = int(re.search(r'(\d+)$', true)[1])
        self.false = int(re.search(r'(\d+)$', false)[1])

        self.monkey_business = 0

    def do_turn(self, monkeys, lcm):
        while self.items:
            self.monkey_business += 1
            worry_level = Monkey.operation(self.items.pop(0), *self.op)
            worry_level = worry_level % lcm if lcm else worry_level // 3
            reciever = self.true if worry_level % self.test == 0 else self.false
            monkeys[reciever].items.append(worry_level)

    @staticmethod
    def get_business(monkeys, num_turns, lcm=False):
        if lcm:
            lcm = math.lcm(*[monkey.test for monkey in monkeys])
        for _ in range(num_turns):
            for monkey in monkeys:
                monkey.do_turn(monkeys, lcm)

        top, second = sorted(
            [monkey.monkey_business for monkey in monkeys])[-2:]
        return top * second


# generate monkeys
with open('../input.txt') as file:

    p1_monkeys, p2_monkeys = [], []

    while True:
        lines = [file.readline().strip() for _ in range(6)]
        p1_monkeys.append(Monkey(lines))
        p2_monkeys.append(Monkey(lines))
        if not file.readline():
            break

    print("Part 1:", Monkey.get_business(p1_monkeys, num_turns=20))
    print("Part 2:", Monkey.get_business(p2_monkeys, num_turns=10_000, lcm=True))
