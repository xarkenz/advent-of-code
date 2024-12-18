//
// Created by xarkenz on 12/23/22.
//

#include "adventofcode.h"

#define NORTH 0
#define NORTHEAST 1
#define EAST 2
#define SOUTHEAST 3
#define SOUTH 4
#define SOUTHWEST 5
#define WEST 6
#define NORTHWEST 7

const int DX[8] {0, 1, 1, 1, 0, -1, -1, -1};
const int DY[8] {-1, -1, 0, 1, 1, 1, 0, -1};

struct D23Elf {
    Position position, proposal;
};

void day23() {
    std::ifstream input("day23.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day23.txt'\n";
        return;
    }
    Map2D map;
    std::vector<D23Elf> elves;
    std::string line;
    for (int y = 0; input.good(); ++y) {
        std::getline(input, line);
        for (int x = 0; x < line.length(); ++x) {
            if (line[x] == '#')
                elves.push_back({{x + 100, y + 100}});  // negative coordinates in Map2D seem to bug out for some reason
        }
    }
    input.close();
    for (const D23Elf& elf : elves) {
        map.set(elf.position.x, elf.position.y, '#');
    }
    int round;
    bool anyMoved = true;
    for (round = 0; anyMoved; ++round) {
        for (D23Elf& elf : elves) {
            elf.proposal = elf.position;
            bool alone = true;
            bool surroundings[8];
            for (int d = 0; d < 8; ++d) {
                surroundings[d] = map.get(elf.position.x + DX[d], elf.position.y + DY[d]) != ' ';
                if (surroundings[d])
                    alone = false;
            }
            if (alone) {
                continue;
            }
            for (int test = 0; test < 4; ++test) {
                int priority = (test + round) % 4;
                if (priority == 0 && !surroundings[NORTH] && !surroundings[NORTHEAST] && !surroundings[NORTHWEST]) {
                    --elf.proposal.y;
                    break;
                } else if (priority == 1 && !surroundings[SOUTH] && !surroundings[SOUTHEAST] && !surroundings[SOUTHWEST]) {
                    ++elf.proposal.y;
                    break;
                } else if (priority == 2 && !surroundings[WEST] && !surroundings[NORTHWEST] && !surroundings[SOUTHWEST]) {
                    --elf.proposal.x;
                    break;
                } else if (priority == 3 && !surroundings[EAST] && !surroundings[NORTHEAST] && !surroundings[SOUTHEAST]) {
                    ++elf.proposal.x;
                    break;
                }
            }
        }
        for (int i = 0; i < elves.size(); ++i) {
            bool conflict = false;
            for (int j = 0; j < elves.size(); ++j) {
                if (j != i && elves[j].proposal.x == elves[i].proposal.x && elves[j].proposal.y == elves[i].proposal.y) {
                    elves[j].proposal = elves[j].position;
                    conflict = true;
                }
            }
            if (conflict)
                elves[i].proposal = elves[i].position;
        }
        anyMoved = false;
        map.clear();
        for (D23Elf& elf : elves) {
            if (elf.position.x != elf.proposal.x || elf.position.y != elf.proposal.y)
                anyMoved = true;
            elf.position = elf.proposal;
            map.set(elf.position.x, elf.position.y, '#');
        }
        if (round + 1 == 10) {
            int minX = elves[0].position.x, maxX = elves[0].position.x, minY = elves[0].position.y, maxY = elves[0].position.y;
            for (const D23Elf& elf : elves) {
                if (elf.position.x < minX)
                    minX = elf.position.x;
                if (elf.position.x > maxX)
                    maxX = elf.position.x;
                if (elf.position.y < minY)
                    minY = elf.position.y;
                if (elf.position.y > maxY)
                    maxY = elf.position.y;
            }
            int totalArea = (maxX - minX + 1) * (maxY - minY + 1);
            int emptyArea = totalArea - elves.size();
            std::cout << "[23p1] Empty area after 10 rounds: " << emptyArea << std::endl;
        }
    }
    std::cout << "[23p2] First round with no move: " << round << std::endl;
}