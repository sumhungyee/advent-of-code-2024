#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>

struct Mem {
    int idx;
    bool occupied;
};


int main() {
    std::ifstream file("input.txt");
    std::string data;
    std::vector<Mem> memspace;
    
    while (file >> data) {}

    bool occupied = true;
    int idx = 0;
    for (char c: data) {
        int repeats = c - '0';
        if (occupied) {
            for (int i = 0; i < repeats; i++) {
                memspace.push_back({idx, true});
            }
            idx++;
        } else {
            for (int i = 0; i < repeats; i++) memspace.push_back({-1, false});
        }

        occupied = !occupied;
    }

    int last = memspace.size() - 1;
    while (!memspace[last].occupied) last--;
    int first = 0;
    long long results = 0;
    while (first < last) {
        if (!memspace[first].occupied) {
         
            Mem temp = memspace[last];
            memspace[last] = memspace[first];
            memspace[first] = temp;
            
            while (!memspace[last].occupied) last--;
        }

        first++;
    }

    first = 0;
    while (memspace[first].occupied) results += memspace[first].idx * first++;
    std::cout << results;
    return 0;
}


