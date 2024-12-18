//
// Created by xarkenz on 12/08/22.
//

#include "adventofcode.h"

void day08() {
    std::ifstream input("day08.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day08.txt'\n";
        return;
    }
    std::vector<std::string> trees;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        trees.push_back(line);
    }
    int visibleCount = 0, maxScenicScore = 0;
    for (int r = 0; r < trees.size(); ++r) {
        for (int c = 0; c < trees[r].length(); ++c) {
            char tree = trees[r][c];
            bool visible0 = true, visible1 = true, visible2 = true, visible3 = true;
            int scenicScore = 1, distance = 0;
            for (int i = r - 1; i >= 0; --i) {
                ++distance;
                if (trees[i][c] >= tree) {
                    visible0 = false;
                    break;
                }
            }
            scenicScore *= distance;
            distance = 0;
            for (int i = r + 1; i < trees.size(); ++i) {
                ++distance;
                if (trees[i][c] >= tree) {
                    visible1 = false;
                    break;
                }
            }
            scenicScore *= distance;
            distance = 0;
            for (int i = c - 1; i >= 0; --i) {
                ++distance;
                if (trees[r][i] >= tree) {
                    visible2 = false;
                    break;
                }
            }
            scenicScore *= distance;
            distance = 0;
            for (int i = c + 1; i < trees[r].length(); ++i) {
                ++distance;
                if (trees[r][i] >= tree) {
                    visible3 = false;
                    break;
                }
            }
            scenicScore *= distance;
            if (visible0 || visible1 || visible2 || visible3) {
                ++visibleCount;
            }
            if (scenicScore > maxScenicScore) {
                maxScenicScore = scenicScore;
            }
        }
    }
    input.close();
    std::cout << "[08p1] Trees visible: " << visibleCount << std::endl;
    std::cout << "[08p2] Max scenic score: " << maxScenicScore << std::endl;
}