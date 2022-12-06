#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

// Values of Rock, Paper and Scissors
std::unordered_map<char, int> vals = {{
    {'A', 1},
    {'B', 2},
    {'C', 3},
    {'X', 1},
    {'Y', 2},
    {'Z', 3},
}};

// Retrieve the score of the match
std::unordered_map<char, std::unordered_map<char, int>> get_result = {{
    {'A', {{'X', 3}, {'Y', 6}, {'Z', 0}}},
    {'B', {{'X', 0}, {'Y', 3}, {'Z', 6}}},
    {'C', {{'X', 6}, {'Y', 0}, {'Z', 3}}},
}};

// Determine recommended action (Part 2)
std::unordered_map<char, std::unordered_map<char, char>> actions = {{
    {'X', {{'A', 'Z'}, {'B', 'X'}, {'C', 'Y'}}},
    {'Y', {{'A', 'X'}, {'B', 'Y'}, {'C', 'Z'}}},
    {'Z', {{'A', 'Y'}, {'B', 'Z'}, {'C', 'X'}}},
}};

int main() {
    auto file = std::ifstream("../input.txt");
    std::string line;

    size_t part_1_sum = 0, part_2_sum = 0;

    while (std::getline(file, line)) {
        char opponent = line[0], me = line[2];

        // Part 1
        part_1_sum += vals[me] + get_result[opponent][me];

        // Part 2
        char p2_action = actions[me][opponent];
        part_2_sum += vals[p2_action] + get_result[opponent][p2_action];
    }

    std::cout
        << "Part 1: "
        << part_1_sum
        << std::endl;

    std::cout
        << "Part 2: "
        << part_2_sum
        << std::endl;
}