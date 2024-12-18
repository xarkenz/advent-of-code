//
// Created by xarkenz on 12/01/22.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <deque>
#include <functional>

void day01();
void day02();
void day03();
void day04();
void day05();
void day06();
void day07();
void day08();
void day09();
void day10();
void day11();
void day12();
void day13();
void day14();
void day15();
void day16();
void day17();
void day18();
void day19();
void day20();
void day21();
void day22();
void day23();
void day24();
void day25();

int floorMod(int a, int b);
int64_t floorMod64(int64_t a, int64_t b);

struct Position {
    int x = 0, y = 0;
};

struct Map2D {
    struct Row {
        std::string data;
        int offset = 0;
    };
    std::vector<Row> rows;
    int offset = 0;
    char get(int x, int y);
    void set(int x, int y, char c);
    void clear();
    void print(char lead = ' ');
};