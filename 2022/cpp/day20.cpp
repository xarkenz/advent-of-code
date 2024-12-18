//
// Created by xarkenz on 12/20/22.
//

#include "adventofcode.h"

void day20p1() {
    std::ifstream input("day20.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day20.txt'\n";
        return;
    }
    std::vector<int> numbers;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        if (!line.empty())
            numbers.push_back(std::stoi(line));
    }
    input.close();
    int listSize = numbers.size();
    std::vector<int> indices(listSize, 0);
    for (int index = 0; index < listSize; ++index) {
        indices[index] = index;
    }
    for (int index = 0; index < listSize; ++index) {
        int start = 0;
        while (indices[start] != index) {
            ++start;
        }
        int number = numbers[start];
        int target = floorMod(start + number, listSize - 1);
        while (start < target) {
            numbers[start] = numbers[start + 1];
            indices[start] = indices[start + 1];
            ++start;
        }
        while (start > target) {
            numbers[start] = numbers[start - 1];
            indices[start] = indices[start - 1];
            --start;
        }
        numbers[start] = number;
        indices[start] = index;
    }
    int zeroIndex = 0;
    while (numbers[zeroIndex] != 0) {
        ++zeroIndex;
    }
    int coordinateSum = numbers[floorMod(zeroIndex + 1000, listSize)]
                      + numbers[floorMod(zeroIndex + 2000, listSize)]
                      + numbers[floorMod(zeroIndex + 3000, listSize)];
    std::cout << "[20p1] Sum of coordinates (raw): " << coordinateSum << std::endl;
}

void day20p2() {
    std::ifstream input("day20.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day20.txt'\n";
        return;
    }
    std::vector<int64_t> numbers;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        if (!line.empty()) {
            numbers.push_back(std::stoi(line));
            numbers.back() *= 811589153;
        }
    }
    input.close();
    int listSize = numbers.size();
    std::vector<int> indices(listSize, 0);
    for (int index = 0; index < listSize; ++index) {
        indices[index] = index;
    }
    for (int mix = 0; mix < 10; ++mix) {
        for (int index = 0; index < listSize; ++index) {
            int start = 0;
            while (indices[start] != index) {
                ++start;
            }
            int64_t number = numbers[start];
            int target = floorMod64(start + number, listSize - 1);
            while (start < target) {
                numbers[start] = numbers[start + 1];
                indices[start] = indices[start + 1];
                ++start;
            }
            while (start > target) {
                numbers[start] = numbers[start - 1];
                indices[start] = indices[start - 1];
                --start;
            }
            numbers[start] = number;
            indices[start] = index;
        }
    }
    int zeroIndex = 0;
    while (numbers[zeroIndex] != 0) {
        ++zeroIndex;
    }
    int64_t coordinateSum = numbers[floorMod(zeroIndex + 1000, listSize)]
                          + numbers[floorMod(zeroIndex + 2000, listSize)]
                          + numbers[floorMod(zeroIndex + 3000, listSize)];
    std::cout << "[20p2] Sum of coordinates (decrypted): " << coordinateSum << std::endl;
}

void day20() {
    day20p1();
    day20p2();
}