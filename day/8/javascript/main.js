const getInput = require("../../../util/getInput.js");

const directions = [
  [0, -1],
  [0, 1],
  [-1, 0],
  [1, 0],
];

function is_in_forest(x, y, forest) {
  return 0 <= y && y < forest.length && 0 <= x && x < forest[0].length;
}

function get_tree_stats(location, forest) {
  const scores = [];
  is_visible = false;

  for (const direction of directions) {
    let [x, y] = location;
    let distance = 0;
    height = parseInt(forest[y][x]);

    while (true) {
      x += direction[0];
      y += direction[1];

      if (!is_in_forest(x, y, forest)) {
        is_visible = true;
        break;
      }

      ++distance;

      if (parseInt(forest[y][x]) >= height) break;
    }
    scores.push(distance);
  }

  return [is_visible, scores.reduce((acc, cur) => acc * cur, 1)];
}

async function main() {
  const input = await getInput();
  const trees = input.split("\r\n").map((line) => line.split(""));

  let num_visible = 0;
  const scenic_scores = [];

  for (let y = 0; y < trees.length; ++y) {
    for (let x = 0; x < trees[0].length; ++x) {
      const [is_visible, score] = get_tree_stats([x, y], trees);
      if (is_visible) ++num_visible;
      scenic_scores.push(score);
    }
  }

  console.log(`Part 1: ${num_visible}`);
  console.log(`Part 2: ${Math.max(...scenic_scores)}`);
}

main();
