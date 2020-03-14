struct Point {
    int r;
    int c;
};

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        // search strategy: right -> bottom -> left -> top
        int R = grid.size();
        if (grid.size() == 0) return 0;
        int C = grid[0].size();
        
        stack<struct Point> s; // push which node to visit next
        
        int num = 0;
        
        vector<vector<bool>> visited(R, vector<bool>(C));
        struct Point p;
        
        
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if(!visited[r][c] && grid[r][c] == '1'){
                    p.r = r;
                    p.c = c;
                    s.push(p);
                    num++;
                } else continue;
                // Depth-First-Search
                while (s.size() > 0) {
                    struct Point p = s.top();
                    s.pop();
                    visited[p.r][p.c] = true;
                    struct Point q;
                    if (p.c < C-1) {
                        if (!visited[p.r][p.c+1] && grid[p.r][p.c+1] == '1') {
                            q.r = p.r;
                            q.c = p.c+1;
                            visited[q.r][q.c] = true;
                            s.push(q);
                        }
                    }
                    if (p.r < R-1) {
                        if (!visited[p.r+1][p.c] && grid[p.r+1][p.c] == '1') {
                            q.r = p.r+1;
                            q.c = p.c;
                            visited[q.r][q.c] = true;
                            s.push(q);
                        }
                    }
                    if (p.c > 0) {
                        if (!visited[p.r][p.c-1] && grid[p.r][p.c-1] == '1') {
                            q.r = p.r;
                            q.c = p.c-1;
                            visited[q.r][q.c] = true;
                            s.push(q);
                        }
                    }
                    if (p.r > 0) {
                        if(!visited[p.r-1][p.c] && grid[p.r-1][p.c] == '1') {
                            q.r = p.r-1;
                            q.c = p.c;
                            visited[q.r][q.c] = true;
                            s.push(q);
                        }
                    }
                }
            }
        }
        return num;
    }
};
