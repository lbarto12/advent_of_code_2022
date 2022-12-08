const getInput = require("../../../util/getInput.js");

const arrSum = (arr) => arr.reduce((a, b) => a + b, 0);

var idx = 0;

function get_files(file) {
  const files = [];
  let this_dir_size = 0;

  while (true) {
    const line = file[idx++];
    if (!line || line.startsWith("$ cd ..")) break;

    if ((find_file_size = line.match(/(\d+)/))) {
      this_dir_size += parseInt(find_file_size[1]);
    } else if (line.startsWith("$ cd")) {
      const [sub_size, sub_files] = get_files(file);
      this_dir_size += sub_size;
      files.push(...sub_files);
    }
  }
  return [this_dir_size, [this_dir_size, ...files]];
}

async function main() {
  const input = await getInput();
  const lines = input.split("\r\n");

  const [total_size, files] = get_files(lines);

  // Part 1
  console.log(`Part 1: ${arrSum(files.filter((f) => f < 100000))}`);

  // Part 2
  const disk_size = 70000000;
  const required_space = 30000000;

  files.sort((a, b) => a - b);
  files.every((file) => {
    if (disk_size - total_size + file >= required_space) {
      console.log(`Part 2: ${file}`);
      return false;
    }
    return true;
  });
}

main();
