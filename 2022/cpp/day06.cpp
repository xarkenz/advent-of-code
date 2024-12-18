//
// Created by xarkenz on 12/06/22.
//

#include "adventofcode.h"

void day06p1() {
    std::ifstream input("day06.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day06.txt'\n";
        return;
    }
    int packetMarker = 0;
    char c1 = 0, c2 = 0, c3 = 0, c4 = 0;
    while (input.good()) {
        c4 = c3;
        c3 = c2;
        c2 = c1;
        input.get(c1);
        ++packetMarker;
        if (c4 && c1 != c2 && c1 != c3 && c1 != c4 && c2 != c3 && c2 != c4 && c3 != c4) {
            break;
        }
    }
    input.close();
    std::cout << "[06p1] Start of packet: " << packetMarker << std::endl;
}

void day06p2() {
    std::ifstream input("day06.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day06.txt'\n";
        return;
    }
    int messageMarker = 0;
    std::deque<char> sequence;
    char character;
    while (input.good()) {
        input.get(character);
        ++messageMarker;
        sequence.push_back(character);
        if (sequence.size() > 14) {
            sequence.pop_front();
            bool allUnique = true;
            for (size_t i = 0; i < sequence.size(); ++i) {
                for (size_t j = i + 1; j < sequence.size(); ++j) {
                    if (sequence[i] == sequence[j]) {
                        allUnique = false;
                        break;
                    }
                }
                if (!allUnique) {
                    break;
                }
            }
            if (allUnique) {
                break;
            }
        }
    }
    input.close();
    std::cout << "[06p2] Start of message: " << messageMarker << std::endl;
}

void day06() {
    day06p1();
    day06p2();
}