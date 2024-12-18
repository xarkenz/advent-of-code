//
// Created by xarkenz on 12/21/22.
//

#include "adventofcode.h"

struct D21Monkey {
    std::string name;
    char job;
    int num1, num2;
};

int64_t d21Evaluate(const std::vector<D21Monkey>& monkeys, int index, int level = 0) {
    if (monkeys.at(index).job == 'n') {
        return monkeys[index].num1;
    }
    int64_t leftNumber = d21Evaluate(monkeys, monkeys[index].num1, level + 1);
    int64_t rightNumber = d21Evaluate(monkeys, monkeys[index].num2, level + 1);
    //printf("%s: computing %s(%ld) %c %s(%ld)\n", monkeys[index].name.c_str(), monkeys[monkeys[index].num1].name.c_str(), leftNumber, monkeys[index].job, monkeys[monkeys[index].num2].name.c_str(), rightNumber);
    switch (monkeys[index].job) {
        default:
        case '+': return leftNumber + rightNumber;
        case '-': return leftNumber - rightNumber;
        case '*': return leftNumber * rightNumber;
        case '/': return leftNumber / rightNumber;
    }
}

bool d21UsesHuman(const std::vector<D21Monkey>& monkeys, int index) {
    return monkeys.at(index).name == "humn" || (monkeys[index].job != 'n' &&
           (d21UsesHuman(monkeys, monkeys[index].num1) || d21UsesHuman(monkeys, monkeys[index].num2)));
}

int64_t d21HumanNumber(const std::vector<D21Monkey>& monkeys, int index, int64_t targetNumber) {
    if (monkeys.at(index).name == "humn")
        return targetNumber;
    if (d21UsesHuman(monkeys, monkeys[index].num1)) {
        int64_t rightNumber = d21Evaluate(monkeys, monkeys[index].num2), leftNumber;
        switch (monkeys[index].job) {
            default:
            case '+': leftNumber = targetNumber - rightNumber; break;
            case '-': leftNumber = targetNumber + rightNumber; break;
            case '*': leftNumber = targetNumber / rightNumber; break;
            case '/': leftNumber = targetNumber * rightNumber; break;
        }
        return d21HumanNumber(monkeys, monkeys[index].num1, leftNumber);
    } else {
        int64_t leftNumber = d21Evaluate(monkeys, monkeys[index].num1), rightNumber;
        switch (monkeys[index].job) {
            default:
            case '+': rightNumber = targetNumber - leftNumber; break;
            case '-': rightNumber = leftNumber - targetNumber; break;
            case '*': rightNumber = targetNumber / leftNumber; break;
            case '/': rightNumber = leftNumber / targetNumber; break;
        }
        return d21HumanNumber(monkeys, monkeys[index].num2, rightNumber);
    }
}

void day21() {
    std::ifstream input("day21.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day21.txt'\n";
        return;
    }
    std::vector<std::string> names;
    int root;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        if (line.empty())
            continue;
        names.push_back(line.substr(0, 4));
        if (names.back() == "root") {
            root = names.size() - 1;
        }
    }
    input.clear();
    input.seekg(0);
    std::vector<D21Monkey> monkeys;
    while (input.good()) {
        std::getline(input, line);
        if (line.empty())
            continue;
        D21Monkey monkey{};
        monkey.name = line.substr(0, 4);
        if ('0' <= line[6] && line[6] <= '9') {
            monkey.job = 'n';
            monkey.num1 = std::stoi(line.substr(6));
        } else {
            monkey.job = line[11];
            std::string name1 = line.substr(6, 4), name2 = line.substr(13, 4);
            for (int i = 0; i < names.size(); ++i) {
                if (name1 == names[i])
                    monkey.num1 = i;
                else if (name2 == names[i])
                    monkey.num2 = i;
            }
        }
        monkeys.push_back(monkey);
    }
    input.close();
    int64_t rootNumber = d21Evaluate(monkeys, root);
    std::cout << "[21p1] Number yelled by 'root': " << rootNumber << std::endl;
    bool targetLeft = d21UsesHuman(monkeys, monkeys[root].num2);
    int64_t targetNumber = targetLeft ? d21Evaluate(monkeys, monkeys[root].num1) : d21Evaluate(monkeys, monkeys[root].num2);
    int64_t humanNumber = d21HumanNumber(monkeys, targetLeft ? monkeys[root].num2 : monkeys[root].num1, targetNumber);
    std::cout << "[21p2] Number for 'humn' to yell: " << humanNumber << std::endl;
}