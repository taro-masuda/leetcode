using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int left = 0;
        int right = nums.size();
        int out = INT_MIN;
        while (left < right) {
            int max_candidate = accumulate(&nums[left], &nums[right], 0);
            int max_candidate2;
            if (left + 1 != right) {
                max_candidate2 = accumulate(&nums[left+1], &nums[right], 0);
            }
            if (right - 1 != left) {
                max_candidate2 = max(max_candidate2, accumulate(&nums[left], &nums[right-1], 0));
            }
            if(out < max(max_candidate, max_candidate2)) {
                out = max(max_candidate, max_candidate2);
            };
            left++;
            right--;
        }
        return out;
    }
};
