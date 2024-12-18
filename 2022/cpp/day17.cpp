//
// Created by xarkenz on 12/17/22.
//

#include "adventofcode.h"

struct D17State {
    std::vector<std::string> tower;
    int64_t rockCount, storedY;
    int index;
};

void day17() {
    std::ifstream input("day17.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day17.txt'\n";
        return;
    }
    std::deque<D17State> states;
    bool repeatFound = false;
    D17State state1, state2;
    std::vector<std::string> tower;
    std::vector<Position> falling;
    int64_t rockCount = 0, storedY = 0, targetRockCount = 0;
    int index = -1;
    char direction;
    while (!repeatFound || rockCount < targetRockCount) {
        if (falling.empty()) {
            if (rockCount == 2022) {
                std::cout << "[17p1] Tower height (" << rockCount << " rocks): " << (storedY + tower.size()) << std::endl;
            }
            int bottom = tower.size() + 3;
            switch (rockCount % 5) {
                case 0:
                    falling.push_back({2, bottom});
                    falling.push_back({3, bottom});
                    falling.push_back({4, bottom});
                    falling.push_back({5, bottom});
                    break;
                case 1:
                    falling.push_back({3, bottom});
                    falling.push_back({2, bottom + 1});
                    falling.push_back({3, bottom + 1});
                    falling.push_back({4, bottom + 1});
                    falling.push_back({3, bottom + 2});
                    break;
                case 2:
                    falling.push_back({2, bottom});
                    falling.push_back({3, bottom});
                    falling.push_back({4, bottom});
                    falling.push_back({4, bottom + 1});
                    falling.push_back({4, bottom + 2});
                    break;
                case 3:
                    falling.push_back({2, bottom});
                    falling.push_back({2, bottom + 1});
                    falling.push_back({2, bottom + 2});
                    falling.push_back({2, bottom + 3});
                    break;
                case 4:
                    falling.push_back({2, bottom});
                    falling.push_back({3, bottom});
                    falling.push_back({2, bottom + 1});
                    falling.push_back({3, bottom + 1});
                    break;
                default:
                    break;
            }
        }
        if (!input.good()) {
            input.clear();
            input.seekg(0);
            index = -1;
        }
        ++index;
        input.get(direction);
        bool stop = false;
        switch (direction) {
            case '>': {
                for (const Position& pos : falling) {
                    if (pos.x >= 6 || (pos.y < tower.size() && tower[pos.y][pos.x + 1] != ' ')) {
                        stop = true;
                        break;
                    }
                }
                if (stop) break;
                for (Position& pos : falling) {
                    ++pos.x;
                }
                break;
            }
            case '<': {
                for (const Position& pos : falling) {
                    if (pos.x <= 0 || (pos.y < tower.size() && tower[pos.y][pos.x - 1] != ' ')) {
                        stop = true;
                        break;
                    }
                }
                if (stop) break;
                for (Position& pos : falling) {
                    --pos.x;
                }
                break;
            }
            default:
                continue;
        }
        stop = false;
        for (const Position& pos : falling) {
            if (pos.y <= 0 || (pos.y - 1 < tower.size() && tower[pos.y - 1][pos.x] != ' ')) {
                stop = true;
                break;
            }
        }
        if (stop) {
            int maxY = 0;
            for (const Position& pos : falling) {
                if (pos.y > maxY)
                    maxY = pos.y;
                while (pos.y >= tower.size()) {
                    tower.emplace_back(7, ' ');
                }
                tower[pos.y][pos.x] = '0' + rockCount % 5;
            }
            falling.clear();
            ++rockCount;
            for (int dy = 0; dy < 4 && maxY - dy >= 0; ++dy) {
                if (tower[maxY - dy].find_first_of(' ') == std::string::npos) {
                    tower.erase(tower.begin(), tower.begin() + (maxY - dy + 1));
                    storedY += maxY - dy + 1;
                    for (const D17State& state : states) {
                        if (state.tower == tower && state.index == index && state.rockCount % 5 == rockCount % 5) {
                            repeatFound = true;
                            state1 = state;
                            state2 = {tower, rockCount, storedY, index};
                            targetRockCount = rockCount + (1'000'000'000'000 - rockCount) % (rockCount - state.rockCount);
                            states.clear();
                            break;
                        }
                    }
                    if (!repeatFound)
                        states.push_back({tower, rockCount, storedY, index});
                    break;
                }
            }
        } else {
            for (Position& pos : falling) {
                --pos.y;
            }
        }
    }
    input.close();
    int64_t repetitions = (1'000'000'000'000 - state2.rockCount) / (state2.rockCount - state1.rockCount);
    int64_t height = storedY + tower.size() + repetitions * (state2.storedY - state1.storedY);
    std::cout << "[17p2] Tower height (1T rocks): " << height << std::endl;
}