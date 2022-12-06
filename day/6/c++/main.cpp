#include <fstream>
#include <iostream>
#include <set>

size_t getMarkerLocation(const std::string &stream, size_t block_size) {
    auto packet = std::string(block_size, '0');

    for (size_t i = 0; i < stream.size(); ++i) {
        packet.erase(packet.begin());
        packet += stream[i];

        if (std::set<char>(packet.begin(), packet.end()).size() == block_size)
            return i + 1;
    }
}

int main() {
    auto file = std::ifstream("../input.txt");
    std::string line;
    std::getline(file, line);

    std::cout
        << "Part 1: "
        << getMarkerLocation(line, 4) << std::endl;

    std::cout
        << "Part 2: "
        << getMarkerLocation(line, 14) << std::endl;
}