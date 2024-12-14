#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>

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
    visited[curr_y][curr_x] = true;
    size_t modified = 1;

    while (!is_exiting(curr_x, curr_y, rows, cols, direction)) {
        switch (direction) {
            case 0:
                if (map[curr_y - 1][curr_x] == '#') {
                    direction = (direction + 1) % 4;
                } else {
                    curr_y--;
                    if (!visited[curr_y][curr_x]) {
                        modified++;
                        visited[curr_y][curr_x] = true;
                    } 
                }
                break;

            case 1:
                if (map[curr_y][curr_x + 1] == '#') {
                    direction = (direction + 1) % 4;
                } else {
                    curr_x++;
                    if (!visited[curr_y][curr_x]) {
                        modified++;
                        visited[curr_y][curr_x] = true;
                    }
                }
                break;

            case 2:
                if (map[curr_y + 1][curr_x] == '#') {
                        direction = (direction + 1) % 4;
                    } else {
                        curr_y++;
                        if (!visited[curr_y][curr_x]) {
                            modified++;
                            visited[curr_y][curr_x] = true;
                        } 
                    }
                    break;

            case 3:
                if (map[curr_y][curr_x - 1] == '#') {
                        direction = (direction + 1) % 4;
                    } else {
                        curr_x--;
                        if (!visited[curr_y][curr_x]) {
                            modified++;
                            visited[curr_y][curr_x] = true;
                        } 
                    }
                    break;

            default:
                std::cout << "error" << std::endl;
                exit(1);

        }
    }
    std::cout << modified << std::endl;
    return 0;
}

