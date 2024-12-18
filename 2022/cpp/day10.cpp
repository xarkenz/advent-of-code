//
// Created by xarkenz on 12/10/22.
//

#include "adventofcode.h"

void day10() {
    std::ifstream input("day10.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day10.txt'\n";
        return;
    }
    int x = 1, cycle = 1, signalStrength = 0;
    std::string screen, line;
    while (input.good()) {
        std::getline(input, line);
        screen += (cycle - 1) % 40 >= x - 1 && (cycle - 1) % 40 <= x + 1 ? '#' : '.';
        if (cycle % 40 == 0) {
            screen += '\n';
        } else if ((cycle - 20) % 40 == 0) {
            signalStrength += cycle * x;
        }
        ++cycle;
        if (line.substr(0, 4) == "addx") {
            screen += (cycle - 1) % 40 >= x - 1 && (cycle - 1) % 40 <= x + 1 ? '#' : '.';
            if (cycle % 40 == 0) {
                screen += '\n';
            } else if ((cycle - 20) % 40 == 0) {
                signalStrength += cycle * x;
            }
            ++cycle;
            x += std::stoi(line.substr(5));
        }
    }
    input.close();
    std::cout << "[10p1] Signal strength sum: " << signalStrength << std::endl;
    std::cout << "[10p2] Resulting screen:\n" << screen << std::endl;
}