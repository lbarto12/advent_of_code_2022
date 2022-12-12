#include "../../../util/CPPutil.h"
#include <string>
#include <vector>

bool fullyContains(std::vector<int> a, std::vector<int> b) {
    return (a[0] <= b[0] && a[1] >= b[1]) || (b[0] <= a[0] && b[1] >= a[1]);
}

int main() {
    auto lines = ADVENT::getInputLines();

    size_t intersects = 0, contains = 0;

    for (const auto &line : lines) {
        auto ranges = ADVENT::splitStr(line, ',');
        auto e1range = ranges[0], e2range = ranges[1];

        auto e1se = ADVENT::splitStr(e1range, '-');
        auto e2se = ADVENT::splitStr(e2range, '-');

        std::vector<int> e1_i = {std::stoi(e1se[0]), std::stoi(e1se[1])};
        std::vector<int> e2_i = {std::stoi(e2se[0]), std::stoi(e2se[1])};

        if (fullyContains(e1_i, e2_i))
            contains++;

        // Part 2
        std::vector<int> e1 = ADVENT::makeRange(e1_i[0], e1_i[1] + 1);
        std::vector<int> e2 = ADVENT::makeRange(e2_i[0], e2_i[1] + 1);

        if (ADVENT::intersection<int>({e1, e2}))
            intersects++;
    }

    std::cout << "Part 1: " << contains << std::endl;
    std::cout << "Part 2: " << intersects << std::endl;
}