while (!pq.empty()) {
        Loc popped = get<1>(pq.top());
        pq.pop();
        int i = popped.dir, r = popped.r, c = popped.c;
        vector<Loc> verts = {Loc((i + 1) % 4, r, c), Loc((i - 1) % 4, r, c)};
        for (Loc vert: verts) {
            int alt = dist[popped] + 1000;
            if (alt < dist[vert]) {
                prev[vert] = {popped};
                dist[vert] = alt;
                pq.push(make_pair(alt, vert));
            } else if (alt == dist[vert]) {
                prev[vert].push_back(popped);
            }
        }

        Loc nxt(0, 0, 0);
        switch (i) {
            case 0:
                nxt = {i, r, c + 1};
                break;
            case 1:
                nxt = {i, r + 1, c};
                break;
            case 2:
                nxt = {i, r, c - 1};
                break;
            case 3:
                nxt = {i, r - 1, c};
                break;
            default:
                throw std::runtime_error("Invalid direction");
                break;
            if (graph[nxt.dir][nxt.r][nxt.c] == '.') {
                int alt = dist[popped] + 1000;
                if (alt < dist[nxt]) {
                    prev[nxt] = {popped};
                    dist[nxt] = alt;
                    pq.push(make_pair(alt, nxt));
                } else if (alt == dist[nxt]) {
                    prev[nxt].push_back(popped);            
                }
            }
        }
    }
###################################################
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

    if (dist.find(nxt) != dist.end() && dist.find(popped) != dist.end()) {
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
