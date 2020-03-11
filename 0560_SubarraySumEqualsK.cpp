class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int N = nums.size();
        vector<int> sum(N);
        if (N == 0) return 0;
        sum[0] = nums[0];
        for (int i = 1; i < N; i++) {
            sum[i] = sum[i-1] + nums[i];
        }
        
        int count = 0;
        for (int st = 0; st < N; st++) {
            for (int end = st+1; end < N; end++) {
                if (sum[end] - sum[st] == k) count++;
            }
        }
        for (int i = 0; i < N; i++) {
            if (sum[i] == k) count++;
        }
        return count;
    }
};
