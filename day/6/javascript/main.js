const getInput = require("../../../util/getInput.js");

function getMarkerLocation(stream, block_size) {
  let packet = "0".repeat(block_size);
  for (let i = 0; i < stream.length; i++) {
    packet = packet.slice(1, packet.length) + stream[i];
    if ([...new Set(packet)].length === block_size) return i + 1;
  }
}

(async function main() {
  const input = await getInput();
  console.log(`Part 1: ${getMarkerLocation(input, 4)}`);
  console.log(`Part 2: ${getMarkerLocation(input, 14)}`);
})();
