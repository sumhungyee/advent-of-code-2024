#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <chrono>
#include <regex>
#include <cmath>

long long combo(long long n, std::vector<long long>& registers) {
    return (n < 4) ? n : registers[n % 4];
}

std::pair<long long, long long> func(long long ptr, std::vector<long long>& registers, std::vector<long long> inst){
    long long code = inst[ptr];
    long long operand = inst[ptr + 1];
    switch (code) {
        case 0:
            registers[0] = registers[0] >> combo(operand, registers);
            return {INT_MAX, ptr + 2};
        case 1:
            registers[1] = registers[1] ^ operand;
            return {INT_MAX, ptr + 2};
        case 2:
            registers[1] = combo(operand, registers) & 0b111;
            return {INT_MAX, ptr + 2};
        case 3:
            return (!registers[0]) ? std::make_pair(INT_MAX, ptr + 2) : std::make_pair(INT_MAX, operand);
        case 4:
            registers[1] = registers[1] ^ registers[2];
            return {INT_MAX, ptr + 2};
        case 5: // OUTPUTTER
            return {combo(operand, registers) & 0b111, ptr + 2};
        case 6:
            registers[1] = registers[0] >> combo(operand, registers);
            return {INT_MAX, ptr + 2};
        case 7:
            registers[2] = registers[0] >> combo(operand, registers);
            return {INT_MAX, ptr + 2};
        default:
            return {INT_MAX, INT_MAX};
    }
        
}

std::vector<long long> process(std::vector<long long> inst, long long a, long long initialised[]) {
    std::vector<long long> registers(3, 0);
    std::vector<long long> out;
    for (long long i = 0; i < 3; i++) registers[i] = initialised[i];
    if (a != INT_MAX) registers[0] = a;
    long long ptr = 0;
    
    while (0 <= ptr && ptr + 1 < inst.size()) {
        std::pair<long long, long long> pair = func(ptr, registers, inst);
        long long output = std::get<0>(pair);
        ptr = std::get<1>(pair);
        if (output < INT_MAX) out.push_back(output);
    }
    return out;
}

template<typename T>
void print_vec(const std::vector<T>& answer) {
    std::cout << answer[0];
    for (long long a = 1; a < answer.size(); a++) std::cout << "," << answer[a];
    std::cout << std::endl;
}

int main() {

    std::ifstream file("input.txt");
    std::vector<std::string> data;
    std::string line;
    std::string inst_str;
    std::vector<long long> inst;

    long long registers[3];
    long long j = 0;
    while (file >> line) data.push_back(line);   
    
    for (std::string line: data) {
        if (std::regex_match(line, std::regex("\\d+"))) {
            registers[j] = stoi(line);  
            j++;
        } else if (std::regex_match(line, std::regex("(\\d+,)*(\\d+)"))) {
            inst_str = line;
        }
    }
    // less than 9.
    for (char c: line) {
        if (isdigit(c)) {
            inst.push_back(c - '0');
            std::cout << c - '0' << " ";
        }
    }
    std::cout << std::endl;
    std::vector<long long> answer = process(inst, INT_MAX, registers);

    print_vec(answer);
    return 0;
}