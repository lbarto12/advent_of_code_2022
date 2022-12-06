const getInput = require("../../../util/getInput.js");

const arrSum = arr => arr.reduce((a,b) => a + b, 0);

async function main() {
  const input = await getInput();
  
  const elves = input.split("\r\n\r\n").map(load => 
    arrSum(load.split("\r\n").map(food_item => Number(food_item))));

  elves.sort((a, b) => a - b);

  console.log("Part 1: " + elves.slice(-1, elves.length));
  console.log("Part 2: " + arrSum(elves.slice(-3, elves.length)));
}

main();
