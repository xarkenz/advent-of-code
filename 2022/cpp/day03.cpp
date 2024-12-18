//
// Created by xarkenz on 12/03/22.
//

#include "adventofcode.h"

void day03() {
    std::ifstream input("day03.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day03.txt'\n";
        return;
    }
    std::string line;
    int misplacedPriority = 0, badgePriority = 0;
    int groupMember = 0;
    std::string member1, member2;
    while (input.good()) {
        std::getline(input, line);
        if (line.empty()) {
            continue;
        }
        size_t compartmentSize = line.length() / 2;
        for (size_t i = 0; i < compartmentSize; ++i) {
            char itemType = line[i];
            for (size_t j = compartmentSize; j < line.length(); ++j) {
                if (line[j] == itemType) {
                    misplacedPriority += itemType > 'Z' ? itemType - 'a' + 1 : itemType - 'A' + 27;
                    itemType = 0;  // break flag
                    break;
                }
            }
            if (!itemType) {
                break;
            }
        }
        if (groupMember == 0) {
            member1 = line;
        } else if (groupMember == 1) {
            member2 = line;
        } else {
            for (char badgeType : line) {
                bool found = false;
                for (char itemType : member1) {
                    if (itemType == badgeType) {
                        found = true;
                        break;
                    }
                }
                if (found) {
                    found = false;
                    for (char itemType : member2) {
                        if (itemType == badgeType) {
                            found = true;
                            break;
                        }
                    }
                    if (found) {
                        badgePriority += badgeType > 'Z' ? badgeType - 'a' + 1 : badgeType - 'A' + 27;
                        break;
                    }
                }
            }
        }
        groupMember = (groupMember + 1) % 3;
    }
    input.close();
    std::cout << "[03p1] Misplaced priority: " << misplacedPriority << std::endl;
    std::cout << "[03p2] Badge priority: " << badgePriority << std::endl;
}