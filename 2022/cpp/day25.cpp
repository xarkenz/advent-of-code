//
// Created by xarkenz on 12/25/22.
//

#include "adventofcode.h"

int64_t d25ToInt(const std::string& input) {
    int64_t output = 0;
    int64_t place = 1;
    for (int i = input.size() - 1; i >= 0; --i) {
        output += place * (input[i] == '-' ? -1 : input[i] == '=' ? -2 : input[i] - '0');
        place *= 5;
    }
    return output;
}

std::string d25FromInt(int64_t input) {
    std::string output;
    while (input) {
        int64_t digit = (input + 2) % 5 - 2;
        output.insert(0, 1, digit == -1 ? '-' : digit == -2 ? '=' : digit + '0');
        input = (input - digit) / 5;
    }
    return output;
}

void day25() {
    std::ifstream input("day25.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day25.txt'\n";
        return;
    }
    int64_t sum = 0;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        if (line.empty())
            continue;
        sum += d25ToInt(line);
    }
    input.close();
    std::string snafuSum = d25FromInt(sum);
    int64_t snafuCheck = d25ToInt(snafuSum);
    std::cout << "[25p1] SNAFU sum: " << sum << " -> " << snafuSum << " -> " << snafuCheck << std::endl;
    std::cout << "[25p2] Press the button!\n";
}