//
// Created by xarkenz on 12/24/22.
//

#include "adventofcode.h"

struct D24BlizzardMap {
    struct Space {
        bool n = false, e = false, s = false, w = false;
    };
    int width = 0, height = 0;
    std::vector<std::vector<Space>> spaces;
    bool isOpen(int x, int y) {
        return 0 <= x && x < width && 0 <= y && y < height &&
            !spaces[y][x].n && !spaces[y][x].e && !spaces[y][x].s && !spaces[y][x].w;
    }
    void next() {
        for (int x = 0; x < width; ++x) {
            bool wrapN = spaces[0][x].n;
            bool wrapS = spaces[height - 1][x].s;
            for (int i = 1; i < height; ++i) {
                spaces[i - 1][x].n = spaces[i][x].n;
                spaces[height - i][x].s = spaces[height - 1 - i][x].s;
            }
            spaces[height - 1][x].n = wrapN;
            spaces[0][x].s = wrapS;
        }
        for (int y = 0; y < height; ++y) {
            bool wrapW = spaces[y][0].w;
            bool wrapE = spaces[y][width - 1].e;
            for (int i = 1; i < width; ++i) {
                spaces[y][i - 1].w = spaces[y][i].w;
                spaces[y][width - i].e = spaces[y][width - 1 - i].e;
            }
            spaces[y][width - 1].w = wrapW;
            spaces[y][0].e = wrapE;
        }
    }
    std::string toString() {
        std::string output;
        for (const std::vector<Space>& row : spaces) {
            for (const Space& space : row) {
                char element = space.n ? '^' : '.';
                if (space.e) element = element == '.' ? '>' : '2';
                if (space.s) element = element == '.' ? 'v' : element == '2' ? '3' : '2';
                if (space.w) element = element == '.' ? '<' : element == '2' || element == '3' ? element + 1 : '2';
                output.push_back(element);
            }
            output.push_back('\n');
        }
        return output;
    }
};

bool d24ReachedTarget(const D24BlizzardMap& map, const std::deque<Position>& paths, Position target) {
    for (const Position& path : paths)
        if (path.x == target.x && path.y == target.y)
            return true;
    return false;
}

void d24GoTo(D24BlizzardMap& map, int& minutesElapsed, Position start, Position target) {
    std::deque<Position> paths, nextPaths;
    paths.push_back(start);
    while (!d24ReachedTarget(map, paths, target)) {
        if (paths.empty()) {
            while (!map.isOpen(start.x, start.y)) {
                ++minutesElapsed;
                map.next();
            }
            paths.push_back(start);
        } else {
            ++minutesElapsed;
            map.next();
        }
        for (const Position& path : paths) {
            std::vector<Position> branches;
            branches.reserve(5);
            if (map.isOpen(path.x, path.y)) {
                branches.push_back({path.x, path.y});
            }
            if (map.isOpen(path.x + 1, path.y)) {
                branches.push_back({path.x + 1, path.y});
            }
            if (map.isOpen(path.x, path.y + 1)) {
                branches.push_back({path.x, path.y + 1});
            }
            if (map.isOpen(path.x - 1, path.y)) {
                branches.push_back({path.x - 1, path.y});
            }
            if (map.isOpen(path.x, path.y - 1)) {
                branches.push_back({path.x, path.y - 1});
            }
            for (const Position& branch : branches) {
                bool unique = true;
                for (const Position& existingPath : nextPaths) {
                    if (existingPath.x == branch.x && existingPath.y == branch.y) {
                        unique = false;
                        break;
                    }
                }
                if (unique)
                    nextPaths.push_back(branch);
            }
        }
        paths.swap(nextPaths);
        nextPaths.clear();
    }
    ++minutesElapsed;
    map.next();
}

void day24() {
    std::ifstream input("day24.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day24.txt'\n";
        return;
    }
    D24BlizzardMap map;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        if (line.empty() || line[2] == '#')
            continue;
        ++map.height;
        map.width = line.length() - 2;
        map.spaces.emplace_back(map.width);
        for (int x = 0; line[x + 1] != '#'; ++x) {
            switch (line[x + 1]) {
                case '^': map.spaces.back()[x].n = true; break;
                case '>': map.spaces.back()[x].e = true; break;
                case 'v': map.spaces.back()[x].s = true; break;
                case '<': map.spaces.back()[x].w = true; break;
                default: break;
            }
        }
    }
    input.close();
    int minutesElapsed = 0;
    d24GoTo(map, minutesElapsed, {0, 0}, {map.width - 1, map.height - 1});
    std::cout << "[24p1] Fewest minutes elapsed (one trip): " << minutesElapsed << std::endl;
    d24GoTo(map, minutesElapsed, {map.width - 1, map.height - 1}, {0, 0});
    d24GoTo(map, minutesElapsed, {0, 0}, {map.width - 1, map.height - 1});
    std::cout << "[24p2] Fewest minutes elapsed (double back): " << minutesElapsed << std::endl;
}