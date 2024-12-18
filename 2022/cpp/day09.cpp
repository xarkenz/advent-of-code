//
// Created by xarkenz on 12/09/22.
//

#include "adventofcode.h"

void day09() {
    std::ifstream input("day09.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day09.txt'\n";
        return;
    }
    Position knots[] {{0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}};
    std::vector<Position> tail1Visited, tail2Visited;
    std::string num;
    char direction;
    int moves;
    while (input.good()) {
        input.get(direction);
        input.ignore();
        if (!input.good()) {
            break;
        }
        std::getline(input, num);
        moves = std::stoi(num);
        for (int move = 0; move < moves; ++move) {
            switch (direction) {
                case 'U':
                    ++knots[0].y;
                    break;
                case 'D':
                    --knots[0].y;
                    break;
                case 'R':
                    ++knots[0].x;
                    break;
                case 'L':
                    --knots[0].x;
                    break;
                default:
                    break;
            }
            for (int i = 1; i < 10; ++i) {
                Position &lead = knots[i - 1], &knot = knots[i];
                if (lead.x > knot.x + 1) {
                    knot.x = lead.x - 1;
                    knot.y += lead.y == knot.y ? 0 : lead.y > knot.y ? 1 : -1;
                } else if (lead.x < knot.x - 1) {
                    knot.x = lead.x + 1;
                    knot.y += lead.y == knot.y ? 0 : lead.y > knot.y ? 1 : -1;
                } else if (lead.y > knot.y + 1) {
                    knot.x = lead.x;
                    knot.y = lead.y - 1;
                } else if (lead.y < knot.y - 1) {
                    knot.x = lead.x;
                    knot.y = lead.y + 1;
                }
            }
            bool unique = true;
            for (const Position& pos : tail1Visited) {
                if (pos.x == knots[1].x && pos.y == knots[1].y) {
                    unique = false;
                    break;
                }
            }
            if (unique) {
                tail1Visited.push_back(knots[1]);
            }
            unique = true;
            for (const Position& pos : tail2Visited) {
                if (pos.x == knots[9].x && pos.y == knots[9].y) {
                    unique = false;
                    break;
                }
            }
            if (unique) {
                tail2Visited.push_back(knots[9]);
            }
        }
    }
    input.close();
    std::cout << "[09p1] Unique tail spots, n = 2: " << tail1Visited.size() << std::endl;
    std::cout << "[09p2] Unique tail spots, n = 10: " << tail2Visited.size() << std::endl;
}