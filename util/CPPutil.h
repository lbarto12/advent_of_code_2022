#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

namespace ADVENT {

std::string getInput(const std::string &path = "../input.txt") {
    auto file = std::ifstream(path);
    std::string input;
    std::string line;
    while (std::getline(file, line))
        input += line;
    return input;
}

std::vector<std::string> getInputLines(const std::string &path = "../input.txt") {
    auto file = std::ifstream(path);
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line))
        lines.push_back(line);
    return lines;
}

template <typename T>
T intersection(std::vector<std::vector<T>> lists) {
    if (lists.size() == 0)
        return T();

    auto sets = std::vector<std::unordered_set<T>>(lists.size());
    for (int i = 0; i < lists.size(); ++i) {
        std::unordered_set<T> to_set;
        for (const auto &item : lists[i])
            to_set.insert(item);
        sets[i] = to_set;
    }
    for (auto item : sets[0]) {
        bool inAll = true;
        for (const auto &set : sets) {
            if (set.find(item) == set.end()) {
                inAll = false;
                break;
            }
        }
        if (inAll)
            return item;
    }
    return T();
}

std::vector<char> sliceStr(const std::string &str, int start = 0, int end = -1) {
    if (end == -1)
        end = str.size();
    std::vector<char> sliced;
    for (int i = start; i < end; ++i) {
        sliced.push_back(str[i]);
    }
    return sliced;
}

} // namespace ADVENT