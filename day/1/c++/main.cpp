#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {

    auto myfile = std::ifstream("../input.txt");
    std::vector<std::vector<size_t>> elves = {{}};

    std::string line;
    size_t index = 0;

    while (std::getline(myfile, line)) {
        if (line == "") {
            elves.push_back({});
            index++;
        } else {
            elves[index].push_back(std::stoi(line));
        }
    }

    std::vector<size_t> sums;

    for (const auto &elf : elves) {
        size_t sum = 0;
        for (const auto &num : elf)
            sum += num;
        sums.push_back(sum);
    }

    std::sort(sums.begin(), sums.end());

    size_t len = sums.size();

    std::cout << "Part 1: "
              << sums[len - 1]
              << std::endl;
    std::cout << "Part 2: "
              << sums[len - 1] + sums[len - 2] + sums[len - 3]
              << std::endl;
}
