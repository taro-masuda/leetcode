class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int ROW = obstacleGrid.size();
        if (ROW == 0) return 0;
        int COL = obstacleGrid[0].size();
        if (COL == 0) return 1;
        vector<vector<int>> paths(ROW, vector<int>(COL));
        if (obstacleGrid[0][0] == 0) paths[0][0] = 1;
        else return 0;
        for (int r = 0; r < ROW; r++) {
            for (int c = 0; c < COL; c++) {
                if (r==0 && c==0) continue;
                paths[r][c] = 0;
                if (obstacleGrid[r][c] == 1) continue;
                if (r > 0) paths[r][c] += paths[r-1][c];
                if (c > 0) paths[r][c] += paths[r][c-1];
            }
        }
        return paths[ROW-1][COL-1];
    }
};
