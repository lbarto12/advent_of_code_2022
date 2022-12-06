const path = require("path");
const fs = require("fs/promises");
module.exports = () => fs.readFile(path.join("../input.txt"), "utf8");
