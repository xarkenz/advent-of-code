//
// Created by xarkenz on 12/15/22.
//

#include "adventofcode.h"

struct D15Sensor {
    int x, y, range;
};

void day15() {
    std::ifstream input("day15.txt");
    if (!input.is_open()) {
        std::cerr << "Unable to open 'day15.txt'\n";
        return;
    }
    std::vector<D15Sensor> sensors;
    std::vector<Position> beacons;
    std::string line;
    while (input.good()) {
        std::getline(input, line);
        if (line.empty()) {
            continue;
        }
        D15Sensor sensor;
        size_t index = line.find_first_of('=') + 1;
        sensor.x = std::stoi(line.substr(index));
        index = line.find_first_of('=', index) + 1;
        sensor.y = std::stoi(line.substr(index));
        Position beacon;
        index = line.find_first_of('=', index) + 1;
        beacon.x = std::stoi(line.substr(index));
        index = line.find_first_of('=', index) + 1;
        beacon.y = std::stoi(line.substr(index));
        sensor.range = abs(beacon.x - sensor.x) + abs(beacon.y - sensor.y);
        sensors.push_back(sensor);
        beacons.push_back(beacon);
    }
    input.close();
    const int yLevel = 2000000;
    int minX = sensors[0].x, maxX = sensors[0].x;
    for (const D15Sensor& sensor : sensors) {
        int range = sensor.range - abs(yLevel - sensor.y);
        if (range < 0) {
            continue;
        }
        if (sensor.x - range < minX) {
            minX = sensor.x - range;
        }
        if (sensor.x + range > maxX) {
            maxX = sensor.x + range;
        }
    }
    int nonBeaconPositions = 0;
    for (int x = minX; x <= maxX; ++x) {
        for (const D15Sensor& sensor : sensors) {
            int range = sensor.range - abs(yLevel - sensor.y);
            if (range >= 0 && sensor.x - range <= x && x <= sensor.x + range) {
                bool hasBeacon = false;
                for (const Position& beacon : beacons) {
                    if (beacon.x == x && beacon.y == yLevel) {
                        hasBeacon = true;
                        break;
                    }
                }
                if (!hasBeacon) {
                    ++nonBeaconPositions;
                }
                break;
            }
        }
    }
    std::cout << "[15p1] Non-beacon positions: " << nonBeaconPositions << std::endl;
    for (const D15Sensor& sensor : sensors) {
        for (int i = 0; i < 4; ++i) {
            int dx = i == 0 || i == 1 ? 1 : -1, dy = i == 0 || i == 3 ? 1 : -1;
            for (int n = 0; n < sensor.range + 1; ++n) {
                int x = sensor.x + dx * n, y = sensor.y + dy * (sensor.range + 1 - n);
                if (x < 0 || 4000000 < x || y < 0 || 4000000 < y) {
                    continue;
                }
                bool target = true;
                for (const D15Sensor& otherSensor : sensors) {
                    if (abs(x - otherSensor.x) + abs(y - otherSensor.y) <= otherSensor.range) {
                        target = false;
                        break;
                    }
                }
                if (target) {
                    for (const Position& beacon : beacons) {
                        if (beacon.x == x && beacon.y == y) {
                            target = false;
                            break;
                        }
                    }
                    if (target) {
                        long long combined = x;
                        combined *= 4000000;
                        combined += y;
                        std::cout << "[15p2] Found beacon at " << x << ", " << y << ": " << combined << std::endl;
                        return;
                    }
                }
            }
        }
    }
}