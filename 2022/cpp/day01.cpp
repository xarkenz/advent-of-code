//
// Created by xarkenz on 12/01/22.
//

#include "adventofcode.h"

void day01() {
    std::ifstream input("day01.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day01.txt'\n";
        return;
    }
    std::string line;
    long int currentElfCalories = 0, elf1Calories = 0, elf2Calories = 0, elf3Calories = 0;
    while (input.good()) {
        std::getline(input, line);
        if (line.empty()) {
            if (currentElfCalories > elf1Calories) {
                elf3Calories = elf2Calories;
                elf2Calories = elf1Calories;
                elf1Calories = currentElfCalories;
            } else if (currentElfCalories > elf2Calories) {
                elf3Calories = elf2Calories;
                elf2Calories = currentElfCalories;
            } else if (currentElfCalories > elf3Calories) {
                elf3Calories = currentElfCalories;
            }
            currentElfCalories = 0;
        } else {
            currentElfCalories += std::strtol(line.c_str(), nullptr, 10);
        }
    }
    input.close();
    std::cout << "[01p1] Highest Calorie count: " << elf1Calories << std::endl;
    std::cout << "[01p2] Sum of top 3 counts: " << (elf1Calories + elf2Calories + elf3Calories) << std::endl;
}