//
// Created by xarkenz on 12/22/22.
//

#include "adventofcode.h"

void d22Wrap(Map2D& map, int& facing, Position& position) {
    switch (facing) {
        default:
        case 0: {
            if (map.get(position.x + 1, position.y) == ' ') {
                int startX = position.x;
                while (map.get(position.x - 1, position.y) != ' ')
                    --position.x;
                if (map.get(position.x, position.y) == '#')
                    position.x = startX;
            } else if (map.get(position.x + 1, position.y) != '#') {
                ++position.x;
            }
            break;
        }
        case 1: {
            if (map.get(position.x, position.y + 1) == ' ') {
                int startY = position.y;
                while (map.get(position.x, position.y - 1) != ' ')
                    --position.y;
                if (map.get(position.x, position.y) == '#')
                    position.y = startY;
            } else if (map.get(position.x, position.y + 1) != '#') {
                ++position.y;
            }
            break;
        }
        case 2: {
            if (map.get(position.x - 1, position.y) == ' ') {
                int startX = position.x;
                while (map.get(position.x + 1, position.y) != ' ')
                    ++position.x;
                if (map.get(position.x, position.y) == '#')
                    position.x = startX;
            } else if (map.get(position.x - 1, position.y) != '#') {
                --position.x;
            }
            break;
        }
        case 3: {
            if (map.get(position.x, position.y - 1) == ' ') {
                int startY = position.y;
                while (map.get(position.x, position.y + 1) != ' ')
                    ++position.y;
                if (map.get(position.x, position.y) == '#')
                    position.y = startY;
            } else if (map.get(position.x, position.y - 1) != '#') {
                --position.y;
            }
            break;
        }
    }
}

// Couldn't think of a better way to do this. Tailored for input configured like so:
// .01
// .2.
// 34.
// 5..
void d22WrapCube(Map2D& map, int& facing, Position& position) {
    int region;
    if (position.x < 50) {
        region = position.y < 150 ? 3 : 5;
    } else if (position.x < 100) {
        region = position.y < 50 ? 0 : position.y < 100 ? 2 : 4;
    } else {
        region = 1;
    }
    switch (facing) {
        default:
        case 0: {
            if (map.get(position.x + 1, position.y) == ' ') {
                Position startPosition = position;
                switch (region) {
                    case 1: position = {99, 149 - position.y}; facing = 2; break;
                    case 2: position = {position.y + 50, 49}; facing = 3; break;
                    case 4: position = {149, 149 - position.y}; facing = 2; break;
                    case 5: position = {position.y - 100, 149}; facing = 3; break;
                    default: break;
                }
                if (map.get(position.x, position.y) == '#') {
                    position = startPosition;
                    facing = 0;
                }
            } else if (map.get(position.x + 1, position.y) != '#') {
                ++position.x;
            }
            break;
        }
        case 1: {
            if (map.get(position.x, position.y + 1) == ' ') {
                Position startPosition = position;
                switch (region) {
                    case 1: position = {99, position.x - 50}; facing = 2; break;
                    case 4: position = {49, position.x + 100}; facing = 2; break;
                    case 5: position = {position.x + 100, 0}; break;
                    default: break;
                }
                if (map.get(position.x, position.y) == '#') {
                    position = startPosition;
                    facing = 1;
                }
            } else if (map.get(position.x, position.y + 1) != '#') {
                ++position.y;
            }
            break;
        }
        case 2: {
            if (map.get(position.x - 1, position.y) == ' ') {
                Position startPosition = position;
                switch (region) {
                    case 0: position = {0, 149 - position.y}; facing = 0; break;
                    case 2: position = {position.y - 50, 100}; facing = 1; break;
                    case 3: position = {50, 149 - position.y}; facing = 0; break;
                    case 5: position = {position.y - 100, 0}; facing = 1; break;
                    default: break;
                }
                if (map.get(position.x, position.y) == '#') {
                    position = startPosition;
                    facing = 2;
                }
            } else if (map.get(position.x - 1, position.y) != '#') {
                --position.x;
            }
            break;
        }
        case 3: {
            if (map.get(position.x, position.y - 1) == ' ') {
                Position startPosition = position;
                switch (region) {
                    case 0: position = {0, position.x + 100}; facing = 0; break;
                    case 1: position = {position.x - 100, 199}; break;
                    case 3: position = {50, position.x + 50}; facing = 0; break;
                    default: break;
                }
                if (map.get(position.x, position.y) == '#') {
                    position = startPosition;
                    facing = 3;
                }
            } else if (map.get(position.x, position.y - 1) != '#') {
                --position.y;
            }
            break;
        }
    }
}

void day22() {
    std::ifstream input("day22.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day22.txt'\n";
        return;
    }
    Map2D map;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        if (line.empty())
            break;
        int offset = line.find_first_not_of(' ');
        map.rows.push_back({line.substr(offset), offset});
    }
    std::getline(input, line);
    input.close();
    int facing = 0, facing2 = 0;
    Position position{map.rows[0].offset, 0}, position2{map.rows[0].offset, 0};
    for (size_t index = 0; index < line.length(); ++index) {
        if ('0' <= line[index] && line[index] <= '9') {
            int number = line[index] - '0';
            while (index + 1 < line.length() && '0' <= line[index + 1] && line[index + 1] <= '9') {
                number *= 10;
                number += line[++index] - '0';
            }
            for (int i = 0; i < number; ++i) {
                d22Wrap(map, facing, position);
                d22WrapCube(map, facing2, position2);
            }
        } else if (line[index] == 'L') {
            facing = (facing + 3) % 4;
            facing2 = (facing2 + 3) % 4;
        } else if (line[index] == 'R') {
            facing = (facing + 1) % 4;
            facing2 = (facing2 + 1) % 4;
        }
    }
    std::printf("[22p1] Password (wrap): 1000*%d + 4*%d + %d = %d\n", position.y + 1, position.x + 1, facing, 1000*(position.y+1) + 4*(position.x+1) + facing);
    std::printf("[22p2] Password (cube): 1000*%d + 4*%d + %d = %d\n", position2.y + 1, position2.x + 1, facing2, 1000*(position2.y+1) + 4*(position2.x+1) + facing2);
}