//
// Created by xarkenz on 12/02/22.
//

#include "adventofcode.h"

void day02() {
    std::ifstream input("day02.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day02.txt'\n";
        return;
    }
    std::string line;
    int score1 = 0, score2 = 0;
    while (input.good()) {
        std::getline(input, line);
        if (line.length() != 3) {
            continue;
        }
        int otherPick = line[0] - 'A', playerPick1 = line[2] - 'X';
        score1 += playerPick1 + 1;
        if (otherPick == playerPick1) {  // tie
            score1 += 3;
        } else if ((otherPick + 1) % 3 == playerPick1) {  // win
            score1 += 6;
        }
        int playerPick2 = playerPick1 == 0 ? (otherPick + 2) % 3 :  // loss
                          playerPick1 == 1 ? otherPick :  // tie
                          (otherPick + 1) % 3;  // win
        score2 += playerPick2 + 1;
        if (otherPick == playerPick2) {  // tie
            score2 += 3;
        } else if ((otherPick + 1) % 3 == playerPick2) {  // win
            score2 += 6;
        }
    }
    input.close();
    std::cout << "[02p1] Final score: " << score1 << std::endl;
    std::cout << "[02p2] Final score: " << score2 << std::endl;
}
