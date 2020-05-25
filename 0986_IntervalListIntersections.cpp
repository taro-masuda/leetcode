class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
        int idx_a = 0, idx_b = 0;
        vector<vector<int>> intersections;
        while(idx_a < A.size() && idx_b < B.size()) {
            int stt, end;
            stt = max(A[idx_a][0], B[idx_b][0]);
            if (stt <= A[idx_a][1] && stt <= B[idx_b][1]) {
                end = min(A[idx_a][1], B[idx_b][1]);
                vector<int> startend;
                startend.push_back(stt);
                startend.push_back(end);
                intersections.push_back(startend);
            }
            if (A[idx_a][1] == B[idx_b][1]) {
                idx_a++; idx_b++;
            } else if (A[idx_a][1] < B[idx_b][1]) {
                idx_a++;
            } else idx_b++;
        }
        return intersections;
    }
};
