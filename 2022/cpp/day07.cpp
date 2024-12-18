//
// Created by xarkenz on 12/07/22.
//

#include "adventofcode.h"

struct D07File {
    std::string name;
    int size;
    bool isDir;
    D07File* parent;
    std::vector<D07File*> files;
};

int d07SizeSum(D07File* dir) {
    int sizeSum = 0;
    for (D07File* file : dir->files) {
        if (file->isDir) {
            sizeSum += (file->size <= 100000 ? file->size : 0) + d07SizeSum(file);
        }
    }
    return sizeSum;
}

int d07SmallestSpace(D07File* dir, int space) {
    int smallest = dir->size;
    for (D07File* file : dir->files) {
        if (file->isDir && file->size >= space) {
            int wouldFree = d07SmallestSpace(file, space);
            if (wouldFree < smallest) {
                smallest = wouldFree;
            }
        }
    }
    return smallest;
}

void day07() {
    std::ifstream input("day07.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day07.txt'\n";
        return;
    }
    D07File root{"/", 0, true, nullptr};
    D07File* location = &root;
    std::string arg;
    std::getline(input, arg, ' ');
    while (input.good()) {
        std::getline(input, arg);
        if (arg == "ls") {
            while (input.good()) {
                std::getline(input, arg, ' ');
                if (!input.good() || arg == "$") {
                    break;
                } else if (arg == "dir") {
                    std::getline(input, arg);
                    bool exists = false;
                    for (D07File* file : location->files) {
                        if (file->name == arg) {
                            exists = true;
                            break;
                        }
                    }
                    if (!exists) {
                        location->files.push_back(new D07File{arg, 0, true, location});
                    }
                } else {
                    int size = std::stoi(arg);
                    std::getline(input, arg);
                    bool exists = false;
                    for (D07File* file : location->files) {
                        if (file->name == arg) {
                            exists = true;
                            break;
                        }
                    }
                    if (!exists) {
                        location->files.push_back(new D07File{arg, size, false, nullptr});
                        D07File* dir = location;
                        while (dir) {
                            dir->size += size;
                            dir = dir->parent;
                        }
                    }
                }
            }
        } else {
            arg = arg.substr(3);
            if (arg == "/") {
                location = &root;
            } else if (arg == "..") {
                if (location->parent) {
                    location = location->parent;
                }
            } else {
                for (D07File* file : location->files) {
                    if (file->name == arg && file->isDir) {
                        location = file;
                        break;
                    }
                }
            }
            if (input.good()) {
                std::getline(input, arg, ' ');
            }
        }
    }
    input.close();
    std::cout << "[07p1] Sum of sizes <= 100000: " << d07SizeSum(&root) << std::endl;
    std::cout << "[07p2] Smallest directory free: " << d07SmallestSpace(&root, root.size - 40000000) << std::endl;
}