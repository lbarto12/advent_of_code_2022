const getInput = require("../../../util/getInput.js");

const ALL_ASCII = [
  ...Array.from({ length: 26 }, (_, i) => String.fromCharCode(i + 97)),
  ...Array.from({ length: 26 }, (_, i) => String.fromCharCode(i + 65)),
];

const priority = ALL_ASCII.reduce(
  (acc, char, i) => ({ ...acc, [char]: i + 1 }),
  {}
);

const intersect2 = (xs, ys) => xs.filter((x) => ys.some((y) => y === x));
const intersection = (xs, ys, ...rest) =>
  ys === undefined ? xs : intersection(intersect2(xs, ys), ...rest);

(async function main() {
  const input = await getInput();
  const lines = input.split("\r\n");

  // Part 1
  let part_1_sum = 0;

  for (const line of lines) {
    const middle = Math.floor(line.length / 2);
    const [r1, r2] = [line.slice(0, middle), line.slice(middle)];
    part_1_sum += priority[intersection(Array.from(r1), Array.from(r2)).pop()];
  }
  console.log("Part 1:", part_1_sum);

  // Part 2
  let part_2_sum = 0;
  for (let i = 0; i < lines.length; i += 3) {
    const group = lines.slice(i, i + 3).map((line) => Array.from(line));
    part_2_sum += priority[intersection(...group).pop()];
  }
  console.log("Part 2:", part_2_sum);
})();
