from functools import reduce

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def is_in_forest(x, y, forest):
    return 0 <= y < len(forest) and 0 <= x < len(forest[0])


def get_tree_stats(location, forest):
    scores = []
    is_vis = False
    for direction in directions:
        x, y = location
        distance = 0
        height = int(forest[y][x])

        while True:
            if not is_in_forest(x := x + direction[0], y := y + direction[1], forest):
                is_vis = True
                break

            distance += 1

            if int(forest[y][x]) >= height:
                break

        scores.append(distance)
    return is_vis, reduce(lambda a, b: a * b, scores)


with open('../input.txt') as file:

    trees = file.read().split('\n')

    num_visible = 0
    scenic_scores = []

    for i, row in enumerate(trees):
        for j in range(len(row)):
            is_visible, score = get_tree_stats(location=(j, i), forest=trees)
            num_visible += is_visible
            scenic_scores.append(score)

    print(f'Part 1: {num_visible}')
    print(f'Part 2: {max(scenic_scores)}')
