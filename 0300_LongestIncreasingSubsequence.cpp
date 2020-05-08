class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int N = nums.size();
        if (N == 0) return 0;
        vector<int> cnt(N);
        cnt[0] = 1;
        int maxCnt = 1;
        for (int cur = 1; cur < N; cur++) {
            cnt[cur] = 1;
            for (int prev = 0; prev < cur; prev++) {
                if (nums[prev] < nums[cur]) {
                    cnt[cur] = max(cnt[cur], cnt[prev] + 1);
                    maxCnt = max(maxCnt, cnt[cur]);
                }
            }
        }
        return maxCnt;
    }
};
