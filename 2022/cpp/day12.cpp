//
// Created by xarkenz on 12/12/22.
//

#include "adventofcode.h"

void day12p1() {
    std::ifstream input("day12.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day12.txt'\n";
        return;
    }
    std::vector<std::string> map;
    int startRow, startCol, endRow, endCol;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        size_t start = line.find_first_of('S');
        if (start != std::string::npos) {
            startRow = map.size();
            startCol = start;
            line[start] = 'a';
        }
        size_t end = line.find_first_of('E');
        if (end != std::string::npos) {
            endRow = map.size();
            endCol = end;
            line[end] = 'z';
        }
        map.push_back(line);
    }
    input.close();
    const int DR[] = {0, 1, 0, -1};
    const int DC[] = {1, 0, -1, 0};
    std::vector<std::string> frontier(map);
    frontier[startRow][startCol] = '#';
    int steps = 0;
    bool reachedEnd = false;
    while (!reachedEnd) {
        ++steps;
        std::vector<std::string> oldFrontier(frontier);
        for (int r = 0; !reachedEnd && r < map.size(); ++r) {
            for (int c = 0; !reachedEnd && c < map[r].length(); ++c) {
                if (oldFrontier[r][c] == '#') for (int dir = 0; !reachedEnd && dir < 4; ++dir) {
                        char maxNext = map[r][c] + 1;
                        int rd = r + DR[dir], cd = c + DC[dir];
                        if (0 <= rd && rd < map.size() && 0 <= cd && cd < map[rd].length() && frontier[rd][cd] != '#' && 'a' <= map[rd][cd] && map[rd][cd] <= maxNext) {
                            if (rd == endRow && cd == endCol) {
                                frontier[rd][cd] = '@';
                                reachedEnd = true;
                            }
                            frontier[rd][cd] = '#';
                        }
                    }
            }
        }
    }
    std::cout << "[12p1] Minimum distance from 'S': " << steps << std::endl;
}

void day12p2() {
    std::ifstream input("day12.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day12.txt'\n";
        return;
    }
    std::vector<std::string> map;
    int startRow, startCol, endRow, endCol;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        size_t start = line.find_first_of('S');
        if (start != std::string::npos) {
            startRow = map.size();
            startCol = start;
            line[start] = 'a';
        }
        size_t end = line.find_first_of('E');
        if (end != std::string::npos) {
            endRow = map.size();
            endCol = end;
            line[end] = 'z';
        }
        map.push_back(line);
    }
    input.close();
    const int DR[] = {0, 1, 0, -1};
    const int DC[] = {1, 0, -1, 0};
    std::vector<std::string> frontier(map);
    for (int r = 0; r < map.size(); ++r) {
        for (int c = 0; c < map[r].length(); ++c) {
            if (map[r][c] == 'a') {
                frontier[r][c] = '#';
            }
        }
    }
    int steps = 0;
    bool reachedEnd = false;
    while (!reachedEnd) {
        ++steps;
        std::vector<std::string> oldFrontier(frontier);
        for (int r = 0; !reachedEnd && r < map.size(); ++r) {
            for (int c = 0; !reachedEnd && c < map[r].length(); ++c) {
                if (oldFrontier[r][c] == '#') for (int dir = 0; !reachedEnd && dir < 4; ++dir) {
                        char maxNext = map[r][c] + 1;
                        int rd = r + DR[dir], cd = c + DC[dir];
                        if (0 <= rd && rd < map.size() && 0 <= cd && cd < map[rd].length() && frontier[rd][cd] != '#' && 'a' <= map[rd][cd] && map[rd][cd] <= maxNext) {
                            if (rd == endRow && cd == endCol) {
                                frontier[rd][cd] = '@';
                                reachedEnd = true;
                            }
                            frontier[rd][cd] = '#';
                        }
                    }
            }
        }
    }
    std::cout << "[12p2] Minimum distance from any 'a': " << steps << std::endl;
}

void day12() {
    day12p1();
    day12p2();
}