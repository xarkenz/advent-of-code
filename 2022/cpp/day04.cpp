//
// Created by xarkenz on 12/04/22.
//

#include "adventofcode.h"

void day04() {
    std::ifstream input("day04.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day04.txt'\n";
        return;
    }
    std::string number;
    int containedPairs = 0, overlapPairs = 0;
    int elf1Start, elf1End, elf2Start, elf2End;
    while (input.good()) {
        std::getline(input, number, '-');
        elf1Start = std::stoi(number);
        std::getline(input, number, ',');
        elf1End = std::stoi(number);
        std::getline(input, number, '-');
        elf2Start = std::stoi(number);
        std::getline(input, number);
        elf2End = std::stoi(number);
        if ((elf2Start <= elf1Start && elf1End <= elf2End) || (elf1Start <= elf2Start && elf2End <= elf1End)) {
            ++containedPairs;
        }
        if (!(elf1End < elf2Start || elf2End < elf1Start)) {
            ++overlapPairs;
        }
    }
    input.close();
    std::cout << "[04p1] Contained pairs: " << containedPairs << std::endl;
    std::cout << "[04p2] Overlapping pairs: " << overlapPairs << std::endl;
}