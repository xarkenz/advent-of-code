//
// Created by xarkenz on 12/01/22.
//

#include "adventofcode.h"

#include <chrono>
#include <iomanip>

void measureTime(std::function<void()> callee) {
    auto start_time = std::chrono::steady_clock::now();
    callee();
    auto end_time = std::chrono::steady_clock::now();
    std::cout << "Time elapsed: "
        << std::fixed << std::setprecision(3)
        << (std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count() / 1000.0)
        << " ms" << std::endl;
}

std::string getPath(const char* filename) {
    return std::string("../input/") + filename;
}

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
    measureTime(day01);
    measureTime(day02);
    measureTime(day03);
    measureTime(day04);
    measureTime(day05);
    measureTime(day06);
    measureTime(day07);
    measureTime(day08);
    measureTime(day09);
    measureTime(day10);
    measureTime(day11);
    measureTime(day12);
    measureTime(day13);
    measureTime(day14);
    measureTime(day15);
    measureTime(day16);
    measureTime(day17);
    measureTime(day18);
    measureTime(day19);
    measureTime(day20);
    measureTime(day21);
    measureTime(day22);
    measureTime(day23);
    measureTime(day24);
    measureTime(day25);
}