//
// Created by xarkenz on 12/19/22.
//

#include "adventofcode.h"

// Inspired by betaveros (https://github.com/betaveros/advent-of-code-2022/blob/main/p19.noul)

struct D19Parameters {
    int orePerOreBot;
    int orePerClayBot;
    int orePerObsidianBot;
    int clayPerObsidianBot;
    int orePerGeodeBot;
    int obsidianPerGeodeBot;
};

struct D19State {
    int oreRate = 1, clayRate = 0, obsidianRate = 0, geodeRate = 0;
    int ore = 0, clay = 0, obsidian = 0, geodesOpened = 0;
};

int d19BotDelay(const D19State& state, int oreCost, int clayCost, int obsidianCost) {
    int oreDelay = state.ore >= oreCost ? 0 :
        state.oreRate > 0 ? (oreCost - state.ore + state.oreRate - 1) / state.oreRate : -1;
    int clayDelay = state.clay >= clayCost ? 0 :
        state.clayRate > 0 ? (clayCost - state.clay + state.clayRate - 1) / state.clayRate : -1;
    int obsidianDelay = state.obsidian >= obsidianCost ? 0 :
        state.obsidianRate > 0 ? (obsidianCost - state.obsidian + state.obsidianRate - 1) / state.obsidianRate : -1;
    return oreDelay < 0 || clayDelay < 0 || obsidianDelay < 0 ? -1 : std::max(oreDelay, std::max(clayDelay, obsidianDelay));
}

int d19MaxGeodes(const D19Parameters& parameters, int maxGeodes, const D19State& state, int timeLeft) {
    int baselineGeodes = state.geodesOpened + state.geodeRate * timeLeft;
    if (baselineGeodes > maxGeodes) {
        maxGeodes = baselineGeodes;
    } else if (baselineGeodes + timeLeft * (timeLeft - 1) / 2 <= maxGeodes) {
        return maxGeodes;
    }
    if (state.oreRate < parameters.orePerOreBot || state.oreRate < parameters.orePerClayBot || state.oreRate < parameters.orePerObsidianBot || state.oreRate < parameters.orePerGeodeBot) {
        int oreBotDelay = d19BotDelay(state, parameters.orePerOreBot, 0, 0);
        if (0 <= oreBotDelay && oreBotDelay < timeLeft) {
            D19State branchState = state;
            ++branchState.oreRate;
            branchState.ore += (oreBotDelay + 1) * state.oreRate - parameters.orePerOreBot;
            branchState.clay += (oreBotDelay + 1) * state.clayRate;
            branchState.obsidian += (oreBotDelay + 1) * state.obsidianRate;
            branchState.geodesOpened += (oreBotDelay + 1) * state.geodeRate;
            maxGeodes = d19MaxGeodes(parameters, maxGeodes, branchState, timeLeft - oreBotDelay - 1);
        }
    }
    if (state.clayRate < parameters.clayPerObsidianBot) {
        int clayBotDelay = d19BotDelay(state, parameters.orePerClayBot, 0, 0);
        if (0 <= clayBotDelay && clayBotDelay < timeLeft) {
            D19State branchState = state;
            ++branchState.clayRate;
            branchState.ore += (clayBotDelay + 1) * state.oreRate - parameters.orePerClayBot;
            branchState.clay += (clayBotDelay + 1) * state.clayRate;
            branchState.obsidian += (clayBotDelay + 1) * state.obsidianRate;
            branchState.geodesOpened += (clayBotDelay + 1) * state.geodeRate;
            maxGeodes = d19MaxGeodes(parameters, maxGeodes, branchState, timeLeft - clayBotDelay - 1);
        }
    }
    if (state.obsidianRate < parameters.obsidianPerGeodeBot) {
        int obsidianBotDelay = d19BotDelay(state, parameters.orePerObsidianBot, parameters.clayPerObsidianBot, 0);
        if (0 <= obsidianBotDelay && obsidianBotDelay < timeLeft) {
            D19State branchState = state;
            ++branchState.obsidianRate;
            branchState.ore += (obsidianBotDelay + 1) * state.oreRate - parameters.orePerObsidianBot;
            branchState.clay += (obsidianBotDelay + 1) * state.clayRate - parameters.clayPerObsidianBot;
            branchState.obsidian += (obsidianBotDelay + 1) * state.obsidianRate;
            branchState.geodesOpened += (obsidianBotDelay + 1) * state.geodeRate;
            maxGeodes = d19MaxGeodes(parameters, maxGeodes, branchState, timeLeft - obsidianBotDelay - 1);
        }
    }
    int geodeBotDelay = d19BotDelay(state, parameters.orePerGeodeBot, 0, parameters.obsidianPerGeodeBot);
    if (0 <= geodeBotDelay && geodeBotDelay < timeLeft) {
        D19State branchState = state;
        ++branchState.geodeRate;
        branchState.ore += (geodeBotDelay + 1) * state.oreRate - parameters.orePerGeodeBot;
        branchState.clay += (geodeBotDelay + 1) * state.clayRate;
        branchState.obsidian += (geodeBotDelay + 1) * state.obsidianRate - parameters.obsidianPerGeodeBot;
        branchState.geodesOpened += (geodeBotDelay + 1) * state.geodeRate;
        maxGeodes = d19MaxGeodes(parameters, maxGeodes, branchState, timeLeft - geodeBotDelay - 1);
    }
    return maxGeodes;
}

void day19() {
    std::ifstream input("day19.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day19.txt'\n";
        return;
    }
    int blueprint = 0, qualitySum = 0, maxProduct = 1;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        if (line.empty()) continue;
        ++blueprint;
        D19Parameters parameters;
        parameters.orePerOreBot = std::stoi(line.substr(line.find_first_of(' ', 33) + 1));
        parameters.orePerClayBot = std::stoi(line.substr(line.find_first_of(' ', 62) + 1));
        parameters.orePerObsidianBot = std::stoi(line.substr(line.find_first_of(' ', 95) + 1));
        parameters.clayPerObsidianBot = std::stoi(line.substr(line.find_first_of(' ', 105) + 1));
        parameters.orePerGeodeBot = std::stoi(line.substr(line.find_first_of(' ', 137) + 1));
        parameters.obsidianPerGeodeBot = std::stoi(line.substr(line.find_first_of(' ', 147) + 1));
        qualitySum += blueprint * d19MaxGeodes(parameters, 0, {}, 24);
        if (blueprint <= 3)
            maxProduct *= d19MaxGeodes(parameters, 0, {}, 32);
    }
    input.close();
    std::cout << "[19p1] Sum of quality levels: " << qualitySum << std::endl;
    std::cout << "[19p2] Product of max geodes for first 3: " << maxProduct << std::endl;
}