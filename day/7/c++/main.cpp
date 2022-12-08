#include <fstream>
#include <iostream>
#include <regex>
#include <string>
#include <vector>

std::pair<long, std::vector<int>> getFiles(std::ifstream &file) {
    std::vector<int> files;
    long thisDirSize = 0;

    while (true) {

        std::string line;
        std::getline(file, line);

        if (line.empty() || line.find("$ cd ..") == 0)
            break;

        int i = 0;
        std::string numstore;
        while (i < line.size() && std::isdigit(line[i])) {
            numstore += line[i];
            i++;
        }

        if (!numstore.empty()) {
            auto size = std::stoi(numstore);
            thisDirSize += size;
        } else if (line.find("$ cd ") == 0) {
            auto subdir = getFiles(file);
            thisDirSize += subdir.first;
            for (auto &file : subdir.second)
                files.push_back(file);
        }
    }

    files.push_back(thisDirSize);
    return {thisDirSize, files};
}

int main() {
    auto file = std::ifstream("../input.txt");

    auto result = getFiles(file);
    long totalSize = result.first;
    std::vector<int> files = result.second;

    long sumThreshold = 0;

    for (auto &file : files)
        if (file < 100000)
            sumThreshold += file;

    // Part 1
    std::cout << "Part 1: " << sumThreshold << std::endl;

    // Part 2
    const long DISK_SIZE = 70000000;
    const long REQUIRED_SPACE = 30000000;

    std::sort(files.begin(), files.end());

    for (auto &file : files) {
        if (DISK_SIZE - totalSize + file >= REQUIRED_SPACE) {
            std::cout << "Part 2: " << file << std::endl;
            break;
        }
    }
}