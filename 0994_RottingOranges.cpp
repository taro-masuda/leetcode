class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        bool isFreshExist = false;
        bool isFreshEternally = false;
        bool isRottenExist = false;
        bool changed = true;
        bool changedOnce = false;
        int R = grid.size();
        if (R==0) return 0;
        int C = grid[0].size();
        int time = 0;
        while (changed) {
            changed = false;
            vector<vector<int>> nextGrid(R,vector<int>(C));
            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    nextGrid[r][c] = 0;
                }
            }
            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    if (grid[r][c] == 1) isFreshExist = true;
                    if (grid[r][c] == 2) isRottenExist = true;
                    if (grid[r][c] == 2) {
                        int row = min(r+1,R-1);
                        if (grid[row][c] == 1) {
                            nextGrid[row][c] = 2;
                            changed = true;
                        }
                        row = max(r-1,0);
                        if (grid[row][c] == 1) {
                            nextGrid[row][c] = 2;
                            changed = true;
                        }
                        int col = min(c+1, C-1);
                        if (grid[r][col] == 1) {
                            nextGrid[r][col] = 2;
                            changed = true;
                        }
                        col = max(c-1, 0);
                        if (grid[r][col] == 1) {
                            nextGrid[r][col] = 2;
                            changed = true;
                        }
                    }
                    if (changed) changedOnce = true;
                }
            }
            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    if(nextGrid[r][c] == 2) grid[r][c] = 2;
                }
            }
            if (!changed) break;
            time++;
        }
        for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    if(grid[r][c] == 1) isFreshEternally = true;
                }
            }
        if (isFreshExist) {
            if (isFreshEternally) return -1;
            else return time;
        } else return 0;
    }
};
