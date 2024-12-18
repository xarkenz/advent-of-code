//
// Created by xarkenz on 12/13/22.
//

#include "adventofcode.h"

bool d13IsInOrder(std::string left, std::string right) {
    int lDepth = 0, rDepth = 0, l, r;
    for (l = 0, r = 0; l < left.length() && r < right.length(); ++l, ++r) {
        if (left[l] == '[') {
            ++lDepth;
        } else if (left[l] == ']') {
            --lDepth;
        }
        if (right[r] == '[') {
            ++rDepth;
        } else if (right[r] == ']') {
            --rDepth;
        }
        if (left[l] != right[r] || (left[l] == '1' && left[l + 1] == '0') || (right[r] == '1' && right[r + 1] == '0')) {
            if ('0' <= left[l] && left[l] <= '9' && right[r] == '[') {
                left.insert(left.find_first_not_of("0123456789", l), "]");
                left.insert(l, "[");
                ++lDepth;
                continue;
            } else if ('0' <= right[r] && right[r] <= '9' && left[l] == '[') {
                right.insert(right.find_first_not_of("0123456789", r), "]");
                right.insert(r, "[");
                ++rDepth;
                continue;
            }
            if (!('0' <= left[l] && left[l] <= '9' && '0' <= right[r] && right[r] <= '9')) {
                return left[l] == ']';
            }
            int leftNumber = left[l] - '0', rightNumber = right[r] - '0';
            if (left[l + 1] == '0') {
                ++l;
                leftNumber = 10;
            }
            if (right[r + 1] == '0') {
                ++r;
                rightNumber = 10;
            }
            if (leftNumber < rightNumber) {
                return true;
            } else if (leftNumber > rightNumber) {
                return false;
            }
        }
    }
    return false;
}

void day13() {
    std::ifstream input("day13.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day13.txt'\n";
        return;
    }
    int index = 0, indexSum = 0;
    std::vector<std::string> packets{"[[2]]", "[[6]]"};
    std::string left, right;
    while (input.good()) {
        ++index;
        std::getline(input, left);
        std::getline(input, right);
        input.ignore();
        if (d13IsInOrder(left, right)) {
            indexSum += index;
        }
        packets.push_back(left);
        packets.push_back(right);
    }
    input.close();
    std::cout << "[13p1] Sum of indices: " << indexSum << std::endl;
    int marker2, marker6;
    for (int i = 0; i < packets.size(); ++i) {
        for (int j = i + 1; j < packets.size(); ++j) {
            if (!d13IsInOrder(packets[i], packets[j])) {
                std::swap(packets[i], packets[j]);
            }
        }
        if (packets[i] == "[[2]]") {
            marker2 = i + 1;
        } else if (packets[i] == "[[6]]") {
            marker6 = i + 1;
        }
    }
    std::cout << "[13p2] Product of markers: " << (marker2 * marker6) << std::endl;
}