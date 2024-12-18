//
// Created by xarkenz on 12/01/22.
//

#include "adventofcode.h"

int floorMod(int a, int b) {
    int out = a % b;
    return out < 0 ? out + b : out;
}

int64_t floorMod64(int64_t a, int64_t b) {
    int64_t out = a % b;
    return out < 0 ? out + b : out;
}

char Map2D::get(int x, int y) {
    y -= offset;
    if (y < 0 || rows.size() <= y || x < rows[y].offset || rows[y].offset + rows[y].data.length() <= x) {
        return ' ';
    }
    return rows[y].data[x - rows[y].offset];
}

void Map2D::set(int x, int y, char c) {
    if (rows.empty())
        offset = 0;//y;  // Disabled y-offset feature... was causing strange issues
    y -= offset;
    if (y < 0) {
        rows.insert(rows.begin(), -y, {});
        y = 0;
    } else if (rows.size() <= y || rows[y].data.empty()) {
        while (rows.size() <= y) {
            rows.emplace_back();
        }
        rows[y].offset = x;
        rows[y].data.push_back(c);
        return;
    } else if (x < rows[y].offset) {
        rows[y].data.insert(0, rows[y].offset - x, ' ');
        rows[y].offset = x;
    } else if (rows[y].offset + rows[y].data.length() <= x) {
        rows[y].data.append(x - rows[y].offset - rows[y].data.length() + 1, ' ');
    }
    rows[y].data[x - rows[y].offset] = c;
}

void Map2D::clear() {
    std::vector<Row>().swap(rows);
    offset = 0;
}

void Map2D::print(char lead) {
    for (const Row& row : rows) {
        std::cout << std::string(row.offset, lead) << row.data << std::endl;
    }
}

int main() {
    day01();
    day02();
    day03();
    day04();
    day05();
    day06();
    day07();
    day08();
    day09();
    day10();
    day11();
    day12();
    day13();
    day14();
    day15();
    day16();
    day17();
    day18();
    day19();
    day20();
    day21();
    day22();
    day23();
    day24();
    day25();
}