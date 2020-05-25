class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        int N = A.size();
        unordered_map<int,int> mp;
        for (int a = 0; a < N; a++) {
            for (int b = 0; b < N; b++) {
                int val = A[a] + B[b];
                auto i = mp.find(val);
                if (i == mp.end()) {
                    mp[val] = 1;
                } else {
                    mp[val]++;
                }
            }
        }
        
        int count = 0;
        for (int c = 0; c < N; c++) {
            for (int d = 0; d < N; d++) { 
                int val = - C[c] - D[d];
                auto i = mp.find(val);
                if (i != mp.end()) count += mp[val];
            }
        }
        
        return count;
    }
};
