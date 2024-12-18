//
// Created by xarkenz on 12/16/22.
//

#include "adventofcode.h"

struct D16Valve {
    struct Id {
        char c0, c1;
    } id;
    int flowRate;
    std::vector<size_t> next;
    std::vector<int> times;
};

int d16MinimumTime(const std::vector<D16Valve>& valves, size_t start, size_t target) {
    std::vector<bool> search(valves.size(), false);
    search[start] = true;
    for (int time = 1; time <= 30; ++time) {
        std::vector<bool> searchNow(search);
        for (size_t index = 0; index < valves.size(); ++index) {
            if (!searchNow[index]) continue;
            for (size_t next : valves[index].next) {
                if (next == target)
                    return time;
                search[next] = true;
            }
        }
    }
    return 30;
}

int d16MaximumPressure(const std::vector<D16Valve>& valves, size_t index, const std::vector<size_t>& targets, int time) {
    int maximum = 0;
    for (size_t i = 0; i < targets.size(); ++i) {
        std::vector<size_t> newTargets(targets);
        newTargets.erase(newTargets.begin() + i);
        int newTime = time - valves[index].times[targets[i]] - 1;
        int testMaximum = newTime < 0 ? 0 : valves[targets[i]].flowRate * newTime + d16MaximumPressure(valves, targets[i], newTargets, newTime);
        if (testMaximum > maximum)
            maximum = testMaximum;
    }
    return maximum;
}

int d16MaximumPressure2(const std::vector<D16Valve>& valves, size_t start, size_t index, const std::vector<size_t>& targets, int time) {
    int maximum = 0;
    for (size_t i = 0; i < targets.size(); ++i) {
        std::vector<size_t> newTargets(targets);
        newTargets.erase(newTargets.begin() + i);
        int newTime = time - valves[index].times[targets[i]] - 1;
        int testMaximum = newTime < 0 ? 0 : valves[targets[i]].flowRate * newTime + d16MaximumPressure2(valves, start, targets[i], newTargets, newTime);
        if (testMaximum > maximum)
            maximum = testMaximum;
    }
    return maximum ? maximum : d16MaximumPressure(valves, start, targets, 26);
}

void day16() {
    std::ifstream input("day16.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day16.txt'\n";
        return;
    }
    std::vector<D16Valve::Id> valveIds;
    size_t startValve;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        if (!line.empty()) {
            if (line[6] == 'A' && line[7] == 'A') {
                startValve = valveIds.size();
            }
            valveIds.push_back({line[6], line[7]});
        }
    }
    input.clear();
    input.seekg(0);
    std::vector<D16Valve> valves;
    while (input.good()) {
        std::getline(input, line);
        if (!line.empty()) {
            D16Valve valve{{line[6], line[7]}};
            size_t index = line.find_first_of('=') + 1, flowRateLen;
            valve.flowRate = std::stoi(line.substr(index), &flowRateLen);
            index = line.find_first_of(' ', index + flowRateLen + 23) + 1;
            while (index < line.length()) {
                for (size_t i = 0; i < valveIds.size(); ++i) {
                    if (valveIds[i].c0 == line[index] && valveIds[i].c1 == line[index + 1]) {
                        valve.next.push_back(i);
                        break;
                    }
                }
                index += 4;
            }
            valves.push_back(valve);
        }
    }
    input.close();
    std::vector<size_t> pressureValves;
    for (size_t index = 0; index < valves.size(); ++index) {
        if (valves[index].flowRate) {
            pressureValves.push_back(index);
        }
    }
    valves[startValve].times.resize(valves.size());
    for (size_t index : pressureValves) {
        valves[startValve].times[index] = d16MinimumTime(valves, startValve, index);
        valves[index].times.resize(valves.size());
        for (size_t target : pressureValves) {
            valves[index].times[target] = d16MinimumTime(valves, index, target);
        }
    }
    std::cout << "[16p1] Maximum pressure release (alone): " << d16MaximumPressure(valves, startValve, pressureValves, 30) << std::endl;
    // This takes an obnoxiously long time to run ;-;
    std::cout << "[16p2] Maximum pressure release (team): " << d16MaximumPressure2(valves, startValve, startValve, pressureValves, 26) << std::endl;
}