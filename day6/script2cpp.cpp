#include <iostream>
#include <algorithm>
#include <fstream>
#include <unordered_map>
#include <string>
#include <vector>
#include <memory>
#include <set>

bool is_exiting(int curr_x, int curr_y, int rows, int cols, int direction) {
    switch (direction) {
        case 0:
            return (curr_y == 0);
        case 1: // right
            return (curr_x == cols - 1);
        case 2: // down
            return curr_y == rows - 1;
        case 3: // left
            return curr_x == 0;
        default:
            return false; 
    }

}

std::string helper(int curr_x, int curr_y) {
    return std::to_string(curr_x) + ":" + std::to_string(curr_y);
}

void traverse(int curr_x, int curr_y, int direction, int rows, int cols, std::vector<std::string> map, std::pair<int, int> obstacle, std::shared_ptr<int> count) {
    map[std::get<1>(obstacle)][std::get<0>(obstacle)] = '#';

    std::unordered_map<std::string, int> coordmap; 

    while (!is_exiting(curr_x, curr_y, rows, cols, direction)) {
        switch (direction) {
            case 0:
                (map[curr_y - 1][curr_x] == '#') ? (direction = (direction + 1) % 4) : (curr_y--);
                break;

            case 1:
                (map[curr_y][curr_x + 1] == '#') ? (direction = (direction + 1) % 4) : (curr_x++);
                break;

            case 2:
                (map[curr_y + 1][curr_x] == '#') ? (direction = (direction + 1) % 4) : (curr_y++);
                break;

            case 3:
                (map[curr_y][curr_x - 1] == '#') ? (direction = (direction + 1) % 4) : (curr_x--);
                break;

            default:
                std::cout << "error" << std::endl;
                exit(1);
        }


        if (coordmap.count(helper(curr_x, curr_y)) > 0 && coordmap[helper(curr_x, curr_y)] == direction) {
            (*count)++;
            break;
        } else if (coordmap.count(helper(curr_x, curr_y)) == 0) coordmap[helper(curr_x, curr_y)] = direction;
    }
}

int main() {
    std::ifstream file("input.txt");
    std::string data;
    std::vector<std::string> map;
    std::pair<size_t, size_t> tup;
    size_t j = 0;
    while (file >> data) {
        size_t pos = data.find("^");
        if (pos != std::string::npos) tup = {pos, j};
        map.push_back(data);
        j++;
    }

    const int rows = map.size();
    const int cols = map[0].size();
    int curr_x = std::get<0>(tup);
    int curr_y = std::get<1>(tup);
    int direction = 0; // for "up"

    std::vector<std::vector<bool>> visited(rows, std::vector<bool>(cols, false));
    std::vector<std::pair<int, int>> visited_coords;
    
    while (!is_exiting(curr_x, curr_y, rows, cols, direction)) {
        switch (direction) {
            case 0:
                if (map[curr_y - 1][curr_x] == '#') {
                    direction = (direction + 1) % 4;
                } else {
                    curr_y--;
                    if (!visited[curr_y][curr_x]) {
                        visited[curr_y][curr_x] = true;
                        visited_coords.push_back(std::make_pair(curr_x, curr_y));   
                    } 
                }
                break;

            case 1:
                if (map[curr_y][curr_x + 1] == '#') {
                    direction = (direction + 1) % 4;
                } else {
                    curr_x++;
                    if (!visited[curr_y][curr_x]) {
                        visited[curr_y][curr_x] = true;
                        visited_coords.push_back(std::make_pair(curr_x, curr_y));       
                    }
                }
                break;

            case 2:
                if (map[curr_y + 1][curr_x] == '#') {
                        direction = (direction + 1) % 4;
                    } else {
                        curr_y++;
                        if (!visited[curr_y][curr_x]) {
                            visited[curr_y][curr_x] = true;
                            visited_coords.push_back(std::make_pair(curr_x, curr_y));    
                        } 
                    }
                    break;

            case 3:
                if (map[curr_y][curr_x - 1] == '#') {
                        direction = (direction + 1) % 4;
                    } else {
                        curr_x--;
                        if (!visited[curr_y][curr_x]) {
                            visited[curr_y][curr_x] = true;
                            visited_coords.push_back(std::make_pair(curr_x, curr_y));        
                        } 
                    }
                    break;

            default:
                std::cout << "error" << std::endl;
                exit(1);

        }
    }

    std::shared_ptr<int> count = std::make_shared<int>(0);
    for (std::pair obs: visited_coords) {
        traverse(std::get<0>(tup), std::get<1>(tup), 0, rows, cols, map, obs, count);
    }

    std::cout << *count << std::endl;
    return 0;
}

