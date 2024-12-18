#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <vector>
#include <unordered_map>
#include <set>

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
        int dir;
        int r;
        int c;
        Loc(int dir_val, int r_val, int c_val) : dir(dir_val), r(r_val), c(c_val) {}
        void print_loc() {
            std::cout << "(" << dir << ", " << r << ", " << c << ")" << std::endl;
        }
        bool operator==(const Loc& other) const {
            return (dir == other.dir) && (r == other.r) && (c == other.c);
        }
        bool operator!=(const Loc& other) const {
            return !(*this == other);
        }

};

namespace std {
    template <>
    struct hash<Loc> {
        size_t operator()(const Loc& loc) const {
            size_t h1 = std::hash<int>{}(loc.dir);
            size_t h2 = std::hash<int>{}(loc.r);
            size_t h3 = std::hash<int>{}(loc.c);
            return h1 ^ (h2 << 7) ^ (h3 << 17);
        }
    };
}

class Compare {
    public:
        bool operator()(pair<int, Loc> a, pair<int, Loc> b) {
            return get<0>(a) > get<0>(b);
        }
};

pair<unordered_map<Loc, int>, unordered_map<Loc, vector<Loc>>> djikstra(Loc s_loc, vector<vector<vector<char>>>& graph) {
    size_t rows, cols;
    rows = graph[0].size();
    cols = graph[0][0].size();
    unordered_map<Loc, int> dist;
    unordered_map<Loc, vector<Loc>> prev;
    
    std::priority_queue<pair<int, Loc>, std::vector<pair<int, Loc>>, Compare> pq;
    
    dist[s_loc] = 0;
    pq.push(make_pair(0, s_loc));
    for (size_t i = 0; i < 4; i++) {
        for (size_t r = 0; r < rows; r++) {
            for (size_t c = 0; c < cols; c++) {
                Loc v(i, r, c);
                if (v != s_loc && graph[i][r][c] == '.') {
                    dist[v] = INT_MAX;
                    prev[v] = {};
                }
            }
        }
    }

    while (!pq.empty()) {
        Loc popped = pq.top().second;
        pq.pop();
        int i = popped.dir, r = popped.r, c = popped.c;

        vector<Loc> verts = {Loc((i + 1) % 4, r, c), Loc((i - 1 + 4) % 4, r, c)};
        for (Loc vert : verts) {
            int alt = dist[popped] + 1000;
            if (alt < dist[vert]) {
                prev[vert] = {popped};
                dist[vert] = alt;
                pq.push({alt, vert});
            } else if (alt == dist[vert]) {
                prev[vert].push_back(popped);
            }
        }

        Loc nxt(0, 0, 0);
        switch (i) {
            case 0:
                nxt = Loc(i, r, c + 1);
                break;
            case 1:
                nxt = Loc(i, r + 1, c);
                break;
            case 2:
                nxt = Loc(i, r, c - 1);
                break;
            case 3:
                nxt = Loc(i, r - 1, c);
                break;
            default:
                throw std::runtime_error("Invalid direction");
        }

        if (graph[nxt.dir][nxt.r][nxt.c] == '.') {
            int alt = dist[popped] + 1;
            if (alt < dist[nxt]) {
                prev[nxt] = {popped};
                dist[nxt] = alt;
                pq.push({alt, nxt});
            } else if (alt == dist[nxt]) {
                prev[nxt].push_back(popped);
            }
        } 
    }

    return {dist, prev};
}

// east: 0, south: 1, west: 2, north: 3
int main() {

    std::ifstream file("input.txt");
    vector<std::string> data;
    std::string line;
    Loc start(0, 0, 0);
    std::vector<Loc> end_locs;

    vector<vector<vector<char>>> graph = {vector<vector<char>>(), vector<vector<char>>(), vector<vector<char>>(), vector<vector<char>>()};
    while (file >> line) {
        data.push_back(line);
    }
    
    for (int j = 0; j < 4; j++) {
        vector<vector<char>> row;
        
        for (int s = 0; s < data.size(); s++) {
            std::string line = data[s];
            for (int t = 0; t < line.size(); t++) {
                if (line[t] == 'S') {
                    start = {0, s, t}; // starting at the east
                    line[t] = '.';
                }
                if (line[t] == 'E') {
                    end_locs.push_back({j, s, t});
                    line[t] = '.';
                }
            }
            row.push_back(vector<char>(line.begin(), line.end()));
        }
        graph[j] = row;
    }
    // start.print_loc();
    // for (vector<vector<char>> grid: graph) {
    //     print_grid(grid);
    // }
    pair<unordered_map<Loc, int>, unordered_map<Loc, vector<Loc>>> result = djikstra(start, graph);
    unordered_map<Loc, int> dist = get<0>(result);
    unordered_map<Loc, vector<Loc>> prev = get<1>(result);
    int min_dist = INT_MAX;
    for (Loc e: end_locs) {
        if (dist[e] < min_dist) min_dist = dist[e];
    }
    std::cout << min_dist << std::endl;

    vector<Loc> good_dest;
    for (Loc end : end_locs) {
        if (dist[end] == min_dist) {
            good_dest.push_back(end);
        }
    }

    set<pair<int, int>> path_items = {make_pair(start.r, start.c)};
    for (Loc dest : good_dest) {
        vector<Loc> pred = {dest};
        while (find(pred.begin(), pred.end(), start) == pred.end()) {
            vector<Loc> next_pred = {};
            for (Loc p : pred) {
                path_items.insert({p.r, p.c});
                for (Loc a : prev[p]) {
                    next_pred.push_back(a);
                }
            }
            pred = next_pred;
        }
    }
    std::cout << path_items.size() << std::endl;
}