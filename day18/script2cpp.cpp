#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <vector>
#include <unordered_map>
#include <set>
#include <sstream>
#include <unistd.h>

#define N 71
using namespace std;

void print_grid(const vector<vector<char>>& grid) {
    for (std::vector<char> r: grid) {
        for (char c: r) {
            std::cout << c;
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}



class Loc {
    public:
        int x;
        int y;

        Loc(int x_val, int y_val) : x(x_val), y(y_val) {}

        void print_loc() const {
            std::cout << "(" << x << ", " << y << ")" << std::endl;
        }

        bool operator==(const Loc& other) const {
            return (x == other.x) && (y == other.y);
        }

        bool operator!=(const Loc& other) const {
            return !(*this == other);
        }
};


namespace std {
    template <>
    struct hash<Loc> {
        size_t operator()(const Loc& loc) const {
            size_t h1 = std::hash<int>{}(loc.y);
            size_t h2 = std::hash<int>{}(loc.x);
            return h1 ^ (h2 << 7);
        }
    };
}

class Compare {
    public:
        bool operator()(pair<int, Loc> a, pair<int, Loc> b) {
            return get<0>(a) > get<0>(b);
        }
};

void print_exit(vector<vector<char>> grid, unordered_map<Loc, vector<Loc>>& prev,  unordered_map<Loc, int>& dist, Loc end, Loc start) {
    if (dist[end] == INT_MAX) {
        grid[end.y][end.x] = 'X';
        print_grid(grid);
        usleep(200000);
        system("cls"); // sorry for using windows
        return;
    }

    grid[end.y][end.x] = 'O';
    std::vector<Loc> previous = prev[end];
    while (!previous.empty()) {
        Loc curr = previous.at(0);
        grid[curr.y][curr.x] = 'O';
        previous = prev[curr];
    }
    print_grid(grid);
    usleep(200000);
    system("cls");
}

pair<unordered_map<Loc, int>, unordered_map<Loc, vector<Loc>>> djikstra(Loc start, vector<vector<char>>& graph) {
    size_t rows, cols;
    rows = graph.size();
    cols = graph[0].size();
    unordered_map<Loc, int> dist;
    unordered_map<Loc, vector<Loc>> prev;
    
    std::priority_queue<pair<int, Loc>, std::vector<pair<int, Loc>>, Compare> pq;
    
    dist[start] = 0;
    pq.push(make_pair(0, start));
   
    for (size_t y = 0; y < rows; y++) {
        for (size_t x = 0; x < cols; x++) {
            Loc v(x, y);
            if (v != start && graph[y][x] == '.') {
                dist[v] = INT_MAX;
                prev[v] = {};
            }
        }
    }
    while (!pq.empty()) {
        Loc popped = pq.top().second;
        pq.pop();
        int y = popped.y, x = popped.x;

        vector<Loc> temp = {Loc(x + 1, y), Loc(x - 1, y), Loc(x, y - 1), Loc(x, y + 1)};
        vector<Loc> nbrs;
        std::copy_if (temp.begin(), temp.end(), std::back_inserter(nbrs), [&graph](Loc l){return 0 <= l.x && l.x < N && 0 <= l.y && l.y < N && graph[l.y][l.x] == '.';} );
        for (Loc nbr : nbrs) {
            int alt = dist[popped] + 1;
            if (alt < dist[nbr]) {
                prev[nbr] = {popped};
                dist[nbr] = alt;
                pq.push({alt, nbr});
            } else if (alt == dist[nbr]) {
                prev[nbr].push_back(popped);
            }
        }
    }
    return {dist, prev};
}

// east: 0, south: 1, west: 2, north: 3
int main(int argc, const char* argv[]) {
    // not needed, just processing arguments
    bool print = false;
    for(int i = 0; i < argc; i++) if (std::string(argv[i]) == "-p") print = true;

    std::ifstream file("input.txt");
    vector<Loc> data;
    std::string line;
    Loc start(0, 0);
    Loc end(N - 1, N - 1);
    vector<vector<char>> graph(N, std::vector<char>(N, '.'));
    while (file >> line) {
        std::stringstream ss(line);
        int x, y;
        char delim;
        ss >> x >> delim >> y;
        data.push_back(Loc(x, y));
    }

    for (int i = 0; i < data.size(); i++) {
        graph[data[i].y][data[i].x] = '#';
        pair<unordered_map<Loc, int>, unordered_map<Loc, vector<Loc>>> result = djikstra(start, graph);
        unordered_map<Loc, int> dist = get<0>(result);
        unordered_map<Loc, vector<Loc>> prev = get<1>(result);
        if (print) print_exit(graph, prev, dist, end, start); // if you wanna print.
        if (dist[end] == INT_MAX) {
            Loc rip = {data[i].x, data[i].y};
            rip.print_loc();
            break;
        }
    }
}