//
// Created by xarkenz on 12/14/22.
//

#include "adventofcode.h"

void day14p1() {
    std::ifstream input("day14.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day14.txt'\n";
        return;
    }
    Map2D scan;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        int lastX, lastY, x, y;
        size_t numberEnd;
        x = std::stoi(line, &numberEnd);
        line.erase(0, numberEnd + 1);
        y = std::stoi(line, &numberEnd);
        line.erase(0, numberEnd + 4);
        while (!line.empty()) {
            lastX = x;
            lastY = y;
            x = std::stoi(line, &numberEnd);
            line.erase(0, numberEnd + 1);
            y = std::stoi(line, &numberEnd);
            line.erase(0, numberEnd + 4);
            int x1 = x > lastX ? lastX : x, x2 = x > lastX ? x : lastX;
            int y1 = y > lastY ? lastY : y, y2 = y > lastY ? y : lastY;
            for (int tileX = x1; tileX <= x2; ++tileX) {
                scan.set(tileX, y1, '#');
            }
            for (int tileY = y1; tileY <= y2; ++tileY) {
                scan.set(x2, tileY, '#');
            }
        }
    }
    input.close();
    int unitsPlaced = 0;
    bool wasPlaced;
    do {
        wasPlaced = true;
        int x = 500, y = 0;
        while (y < scan.rows.size()) {
            if (scan.get(x, y + 1) == ' ') {
                ++y;
            } else if (scan.get(x - 1, y + 1) == ' ') {
                --x;
                ++y;
            } else if (scan.get(x + 1, y + 1) == ' ') {
                ++x;
                ++y;
            } else {
                scan.set(x, y, 'o');
                ++unitsPlaced;
                break;
            }
        }
        if (y >= scan.rows.size()) {
            wasPlaced = false;
        }
    } while (wasPlaced);
    std::cout << "[14p1] Units of sand placed above abyss: " << unitsPlaced << std::endl;
}

void day14p2() {
    std::ifstream input("day14.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day14.txt'\n";
        return;
    }
    Map2D scan;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        int lastX, lastY, x, y;
        size_t numberEnd;
        x = std::stoi(line, &numberEnd);
        line.erase(0, numberEnd + 1);
        y = std::stoi(line, &numberEnd);
        line.erase(0, numberEnd + 4);
        while (!line.empty()) {
            lastX = x;
            lastY = y;
            x = std::stoi(line, &numberEnd);
            line.erase(0, numberEnd + 1);
            y = std::stoi(line, &numberEnd);
            line.erase(0, numberEnd + 4);
            int x1 = x > lastX ? lastX : x, x2 = x > lastX ? x : lastX;
            int y1 = y > lastY ? lastY : y, y2 = y > lastY ? y : lastY;
            for (int tileX = x1; tileX <= x2; ++tileX) {
                scan.set(tileX, y1, '#');
            }
            for (int tileY = y1; tileY <= y2; ++tileY) {
                scan.set(x2, tileY, '#');
            }
        }
    }
    input.close();
    int lowest = scan.rows.size(), unitsPlaced = 0;
    while (true) {
        int x = 500, y = 0;
        while (true) {
            if (y >= lowest) {
                scan.set(x, y, 'o');
                ++unitsPlaced;
                break;
            } else if (scan.get(x, y + 1) == ' ') {
                ++y;
            } else if (scan.get(x - 1, y + 1) == ' ') {
                --x;
                ++y;
            } else if (scan.get(x + 1, y + 1) == ' ') {
                ++x;
                ++y;
            } else {
                scan.set(x, y, 'o');
                ++unitsPlaced;
                break;
            }
        }
        if (x == 500 && y == 0) {
            break;
        }
    }
    std::cout << "[14p2] Units of sand placed with floor: " << unitsPlaced << std::endl;
}

void day14() {
    day14p1();
    day14p2();
}