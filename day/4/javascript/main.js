const getInput = require("../../../util/getInput.js");

const full_overlap = (a, b) =>
  (a[0] <= b[0] && a[1] >= b[1]) || (b[0] <= a[0] && b[1] >= a[1]);

const intersect2 = (xs, ys) => xs.filter((x) => ys.some((y) => y === x));

const range = (start, end) =>
  [...Array(end - start + 1)].map((_, i) => i + start);

(async function main() {
  const input = await getInput();
  const lines = input.split("\r\n");

  let intersects = 0;
  let contains = 0;

  for (const line of lines) {
    let [e1, e2] = line
      .split(",")
      .map((e) => e.split("-").map((x) => parseInt(x)));

    // Part 1
    if (full_overlap(e1, e2)) contains++;
    if (intersect2(range(...e1), range(...e2)).length != 0) intersects++;
  }

  console.log("Part 1:", contains);
  console.log("Part 2:", intersects);
})();
