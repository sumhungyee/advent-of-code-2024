#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <fstream>
#include <string>
#include <vector>

struct Mem {
    int idx;
    bool occupied;
    int size;
};


std::ostream& operator<<(std::ostream& os, const Mem& m) {
    os << "ID: " << m.idx << ", Size: " << m.size;
    return os;  
}

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
            Mem memory = {idx, true, repeats};
            if (repeats > 0) {
                memspace.push_back(memory);
            }
            
            idx++;
        } else {
            if (repeats > 0) memspace.push_back({-1, false, repeats});
        }
        occupied = !occupied;
    }
    idx--;
    while (idx >= 0) {
        int search = memspace.size() - 1;
        while (memspace.at(search).idx != idx) {
            
            search--;
        }
        
        int candidate_num = search;
        Mem candidate = memspace.at(search);
        int required = candidate.size;

        search = 0;
        while (search < candidate_num && (memspace.at(search).occupied || memspace.at(search).size < required)) {
            search++;
        }

        if (search < candidate_num) {
            int swapper_num = search;
            Mem swapper = memspace.at(search);
            int new_size = swapper.size - required;
            
            if (new_size == 0) {
                memspace[swapper_num] = candidate;
                
            } else {
                memspace[swapper_num].size -= required;
                memspace.insert(memspace.begin() + swapper_num, candidate);
                candidate_num++;
            }

            memspace[candidate_num] = {-1, false, required};
            if (candidate_num + 1 < memspace.size() && !memspace.at(candidate_num + 1).occupied) {
                memspace[candidate_num].size += memspace[candidate_num + 1].size;
                memspace.erase(memspace.begin() + candidate_num + 1);
            }

            if (candidate_num - 1  >= 0 && !memspace.at(candidate_num - 1).occupied) {
                memspace[candidate_num].size += memspace[candidate_num - 1].size;
                memspace.erase(memspace.begin() + candidate_num - 1);
            }
            
        }

        idx--;
        
    }
    int counter = 0;
    long long result = 0;
    for (Mem m: memspace)
    for (int i = 0; i < m.size; i++) {
        result += (m.occupied) ? counter++ * m.idx: 0 * counter++;
    }
    
    std::cout << result << std::endl;
    return 0;
}


