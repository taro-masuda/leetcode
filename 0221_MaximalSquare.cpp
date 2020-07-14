class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int maxSquare = 0;
        int M = matrix.size(); if (M == 0) return maxSquare;
        int N = matrix[0].size(); if (N == 0) return maxSquare;
        int maxlen = 0;
        for (int m = 0; m < M; m++) {
            for (int n = 0; n < N; n++) {
                if (matrix[m][n] == '1') {
                    int curlen = 1;
                    maxlen = max(maxlen, 1);
                    bool flag = true;
                    while (m + curlen < M and n + curlen < N and flag) {
                        for (int w = n; w <= n + curlen; w++) {
                            if (matrix[m + curlen][w] == '0') flag = false;
                        }
                        for (int h = m; h <= m + curlen; h++) {
                            if (matrix[h][n + curlen] == '0') flag = false;
                        }
                        if (flag) curlen++;
                        maxlen = max(maxlen, curlen);
                    }
                }
            }
        }
        return maxlen*maxlen;
    }
};
