//
// Created by xarkenz on 12/11/22.
//

#include "adventofcode.h"

struct D11Monkey {
    std::deque<int> items;
    std::function<int(int)> operation;
    int divideTest;
    int trueMonkey, falseMonkey;
    int turns;
};

void day11p1() {
    // You could say this is cheating and I should have parsed the input... but whatever. Too much effort.
    D11Monkey monkeys[] {
            {{75, 63}, [](int old){return old * 3;}, 11, 7, 2, 0},
            {{65, 79, 98, 77, 56, 54, 83, 94}, [](int old){return old + 3;}, 2, 2, 0, 0},
            {{66}, [](int old){return old + 5;}, 5, 7, 5, 0},
            {{51, 89, 90}, [](int old){return old * 19;}, 7, 6, 4, 0},
            {{75, 94, 66, 90, 77, 82, 61}, [](int old){return old + 1;}, 17, 6, 1, 0},
            {{53, 76, 59, 92, 95}, [](int old){return old + 2;}, 19, 4, 3, 0},
            {{81, 61, 75, 89, 70, 92}, [](int old){return old * old;}, 3, 0, 1, 0},
            {{81, 86, 62, 87}, [](int old){return old + 8;}, 13, 3, 5, 0},
    };
    for (int round = 1; round <= 20; ++round) {
        for (int m = 0; m < 8; ++m) {
            D11Monkey& monkey = monkeys[m];
            while (!monkey.items.empty()) {
                ++monkey.turns;
                monkey.items.front() = monkey.operation(monkey.items.front()) / 3;
                monkeys[monkey.items.front() % monkey.divideTest == 0 ? monkey.trueMonkey : monkey.falseMonkey].items.push_back(monkey.items.front());
                monkey.items.pop_front();
            }
        }
    }
    int mostTurns1 = 0, mostTurns2 = 0;
    for (int m = 0; m < 8; ++m) {
        if (monkeys[m].turns > mostTurns1) {
            mostTurns2 = mostTurns1;
            mostTurns1 = monkeys[m].turns;
        } else if (monkeys[m].turns > mostTurns2) {
            mostTurns2 = monkeys[m].turns;
        }
    }
    std::cout << "[11p1] Monkey business after 20 rounds: " << (mostTurns1 * mostTurns2) << std::endl;
}

struct D11WorryLevel {
    const int TESTS[8] {11, 2, 5, 7, 17, 19, 3, 13};
    int mods[8];
    D11WorryLevel(int x) {
        for (int i = 0; i < 8; ++i) {
            mods[i] = x % TESTS[i];
        }
    }
    void add(int x) {
        for (int i = 0; i < 8; ++i) {
            mods[i] = (mods[i] + x) % TESTS[i];
        }
    }
    void mul(int x) {
        for (int i = 0; i < 8; ++i) {
            mods[i] = (mods[i] * x) % TESTS[i];
        }
    }
    void square() {
        for (int i = 0; i < 8; ++i) {
            mods[i] = (mods[i] * mods[i]) % TESTS[i];
        }
    }
};

struct D11Monkey2 {
    std::deque<D11WorryLevel> items;
    std::function<void(D11WorryLevel&)> operation;
    int trueMonkey, falseMonkey;
    int turns;
};

void day11p2() {
    D11Monkey2 monkeys[] {
            {{{75},{63}}, [](D11WorryLevel& old){old.mul(3);}, 7, 2, 0},
            {{{65},{79},{98},{77},{56},{54},{83},{94}}, [](D11WorryLevel& old){old.add(3);}, 2, 0, 0},
            {{{66}}, [](D11WorryLevel& old){old.add(5);}, 7, 5, 0},
            {{{51},{89},{90}}, [](D11WorryLevel& old){old.mul(19);}, 6, 4, 0},
            {{{75},{94},{66},{90},{77},{82},{61}}, [](D11WorryLevel& old){old.add(1);}, 6, 1, 0},
            {{{53},{76},{59},{92},{95}}, [](D11WorryLevel& old){old.add(2);}, 4, 3, 0},
            {{{81},{61},{75},{89},{70},{92}}, [](D11WorryLevel& old){old.square();}, 0, 1, 0},
            {{{81},{86},{62},{87}}, [](D11WorryLevel& old){old.add(8);}, 3, 5, 0},
    };
    for (int round = 1; round <= 10000; ++round) {
        for (int m = 0; m < 8; ++m) {
            D11Monkey2& monkey = monkeys[m];
            while (!monkey.items.empty()) {
                ++monkey.turns;
                monkey.operation(monkey.items.front());
                monkeys[monkey.items.front().mods[m] == 0 ? monkey.trueMonkey : monkey.falseMonkey].items.push_back(monkey.items.front());
                monkey.items.pop_front();
            }
        }
    }
    int64_t mostTurns1 = 0, mostTurns2 = 0;
    for (int m = 0; m < 8; ++m) {
        if (monkeys[m].turns > mostTurns1) {
            mostTurns2 = mostTurns1;
            mostTurns1 = monkeys[m].turns;
        } else if (monkeys[m].turns > mostTurns2) {
            mostTurns2 = monkeys[m].turns;
        }
    }
    std::cout << "[11p2] Monkey business after 10000 rounds: " << mostTurns1 << " * " << mostTurns2 << " = " << (mostTurns1 * mostTurns2) << std::endl;
}

void day11() {
    day11p1();
    day11p2();
}