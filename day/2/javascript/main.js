const getInput = require("../../../util/getInput.js");

// Values of Rock, Paper and Scissors
const vals = {
  A: 1,
  X: 1,
  B: 2,
  Y: 2,
  C: 3,
  Z: 3,
};

// Retrieve the score of the match
const get_result = {
  A: { Z: 0, X: 3, Y: 6 },
  B: { X: 0, Y: 3, Z: 6 },
  C: { Y: 0, Z: 3, X: 6 },
};

// Determine recommended action (Part 2)
const actions = {
  X: { A: "Z", B: "X", C: "Y" },
  Y: { A: "X", B: "Y", C: "Z" },
  Z: { A: "Y", B: "Z", C: "X" },
};

async function main() {
  const input = (await getInput()).split("\r\n");

  let part_1_sum = 0;
  let part_2_sum = 0;

  for (const line of input) {
    const [opponent, me] = line.split(" ");

    // Part 1
    part_1_sum += vals[me] + get_result[opponent][me];

    // Part 2
    const p2_action = actions[me][opponent];
    part_2_sum += vals[p2_action] + get_result[opponent][p2_action];
  }

  console.log(`Part 1: ${part_1_sum}`);
  console.log(`Part 2: ${part_2_sum}`);
}

main();
