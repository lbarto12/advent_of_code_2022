#include "../../../util/CPPutil.h"
#include <iostream>
#include <unordered_map>
#include <vector>

std::unordered_map<char, int> createPriorities() {
    std::unordered_map<char, int> priorities;
    for (char c = 'a'; c <= 'z'; ++c)
        priorities[c] = c - 'a' + 1;
    for (char c = 'A'; c <= 'Z'; ++c)
        priorities[c] = c - 'A' + 26 + 1;
    return priorities;
}

int main() {
    auto priority = createPriorities();
    auto lines = ADVENT::getInputLines();

    size_t part1Sum = 0;

    for (auto &line : lines) {
        const size_t middle = line.size() / 2;
        auto r1 = ADVENT::sliceStr(line, 0, middle);
        auto r2 = ADVENT::sliceStr(line, middle, line.size());
        part1Sum += priority[ADVENT::intersection<char>({r1, r2})];
    }

    std::cout << "Part 1: " << part1Sum << std::endl;

    // Part 2
    size_t part2Sum = 0;

    for (int i = 0; i < lines.size(); i += 3) {
        std::vector<std::vector<char>> groups = {
            ADVENT::sliceStr(lines[i]),
            ADVENT::sliceStr(lines[i + 1]),
            ADVENT::sliceStr(lines[i + 2]),
        };
        part2Sum += priority[ADVENT::intersection<char>(groups)];
    }

    std::cout << "Part 2: " << part2Sum << std::endl;
}