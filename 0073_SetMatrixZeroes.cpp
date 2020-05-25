class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> rows (m, 0);
        vector<int> cols (n, 0);
        for (int row = 0; row < m; row++){
            for(int col = 0; col < n; col++){
                if (matrix[row][col] == 0){
                    rows[row] += 1;
                    cols[col] += 1;
                }
            }
        }
        for (int row = 0; row < m; row++){
            for(int col = 0; col < n; col++){
                if(rows[row] > 0 || cols[col] > 0) matrix[row][col] = 0;
            }
        }
    }
};
