class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        int M = matrix.size();
        vector<int> ans;
        if (M == 0) return ans;
        int N = matrix[0].size();
        if (N == 0) return ans;
        int m = 0, n = 0;
        bool upper = true;
        while (m < M || n < N) {
            ans.push_back(matrix[m][n]);
            if (upper && (m == 0 || n == N-1)) {
                upper = false;
                if (n < N-1) n++;
                else if (m < M-1) m++;
                else break;
            } else if (!upper && (m == M-1 || n == 0)) {
                upper = true;
                if (m < M-1) m++;
                else if (n < N-1) n++;
                else break;
            } else {
                if (upper) {m--; n++;}
                else {m++; n--;}
            }
        }
        return ans;
    }
};
