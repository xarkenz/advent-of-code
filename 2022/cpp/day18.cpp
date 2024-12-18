//
// Created by xarkenz on 12/18/22.
//

#include "adventofcode.h"

void day18() {
    std::ifstream input("day18.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day18.txt'\n";
        return;
    }
    std::vector<std::vector<std::vector<bool>>> model;
    int maxX = 0, maxY = 0, maxZ = 0;
    std::string num;
    while (input.good()) {
        int x, y, z;
        std::getline(input, num, ',');
        if (num.empty()) continue;
        x = std::stoi(num);
        std::getline(input, num, ',');
        y = std::stoi(num);
        std::getline(input, num);
        z = std::stoi(num);
        if (x > maxX)
            maxX = x;
        if (y > maxY)
            maxY = y;
        if (z > maxZ)
            maxZ = z;
        while (x >= model.size())
            model.emplace_back();
        while (y >= model[x].size())
            model[x].emplace_back();
        while (z >= model[x][y].size())
            model[x][y].push_back(false);
        model[x][y][z] = true;
    }
    input.close();
    for (int x = 0; x <= maxX; ++x) {
        while (model[x].size() <= maxY) {
            model[x].emplace_back();
        }
        for (int y = 0; y <= maxY; ++y) {
            while (model[x][y].size() <= maxZ) {
                model[x][y].push_back(false);
            }
        }
    }
    std::vector<std::vector<std::vector<bool>>> air(maxX + 1, std::vector<std::vector<bool>>(maxY + 1, std::vector<bool>(maxZ + 1, false)));
    bool moved = true;
    while (moved) {
        moved = false;
        for (int x = 0; x <= maxX; ++x) {
            for (int y = 0; y <= maxY; ++y) {
                for (int z = 0; z <= maxZ; ++z) {
                    if (air[x][y][z] || model[x][y][z])
                        continue;
                    if (x == 0 || air[x - 1][y][z] || x == maxX || air[x + 1][y][z] || y == 0 || air[x][y - 1][z] || y == maxY || air[x][y + 1][z] || z == 0 || air[x][y][z - 1] || z == maxZ || air[x][y][z + 1]) {
                        air[x][y][z] = true;
                        moved = true;
                    }
                }
            }
        }
    }
    int totalSurfaceArea = 0, exteriorSurfaceArea = 0;
    for (int x = 0; x <= maxX; ++x) {
        for (int y = 0; y <= maxY; ++y) {
            for (int z = 0; z <= maxZ; ++z) {
                if (!model[x][y][z])
                    continue;
                if (x == 0 || !model[x - 1][y][z])
                    ++totalSurfaceArea;
                if (x == maxX || !model[x + 1][y][z])
                    ++totalSurfaceArea;
                if (y == 0 || !model[x][y - 1][z])
                    ++totalSurfaceArea;
                if (y == maxY || !model[x][y + 1][z])
                    ++totalSurfaceArea;
                if (z == 0 || !model[x][y][z - 1])
                    ++totalSurfaceArea;
                if (z == maxZ || !model[x][y][z + 1])
                    ++totalSurfaceArea;
                if (x == 0 || air[x - 1][y][z])
                    ++exteriorSurfaceArea;
                if (x == maxX || air[x + 1][y][z])
                    ++exteriorSurfaceArea;
                if (y == 0 || air[x][y - 1][z])
                    ++exteriorSurfaceArea;
                if (y == maxY || air[x][y + 1][z])
                    ++exteriorSurfaceArea;
                if (z == 0 || air[x][y][z - 1])
                    ++exteriorSurfaceArea;
                if (z == maxZ || air[x][y][z + 1])
                    ++exteriorSurfaceArea;
            }
        }
    }
    std::cout << "[18p1] Total surface area: " << totalSurfaceArea << std::endl;
    std::cout << "[18p2] Exterior surface area: " << exteriorSurfaceArea << std::endl;
}