class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<vector<int>> cost(grid.size(), vector<int>(grid[0].size(), 0));
        cost[0][0] = grid[0][0];
        for (int r = 0; r < grid.size(); r++){
            for(int c = 0; c < grid[0].size(); c++){
                if(r > 0 && c > 0) {
                    cost[r][c] = min(cost[r-1][c], cost[r][c-1]) + grid[r][c];
                } else if (r == 0 && c > 0){
                    cost[r][c] = cost[r][c-1] + grid[r][c];
                } else if (c == 0 && r > 0) {
                    cost[r][c] = cost[r-1][c] + grid[r][c];
                }
            }
        }
        return cost[grid.size()-1][grid[0].size()-1];
    }
};
