class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int N = nums.size();
        if (N == 0) return 0;
        if (N == 1) {
            if (nums[0] < target) return 1;
            else return 0;
        }
        if (N == 2) {
            if (nums[0] < target) {
                if (target < nums[1]) {
                    return 1;
                } else {
                    if (target == nums[1]) return 1;
                    else return 2;
                }
            } else return 0;
        }
        int left = 0, right = N;
        int mid = (left + right) / 2;
        while (left < right) {
            if (nums[mid] == target) return mid;
            if (left == N-1) {
                if (nums[left] < target) return left+1;
                else return left;
            }
            if (mid == N-1) {
                if (nums[mid] < target) return mid+1;
                else return mid-1;
            }
            if (right == 1) {
                if (target < nums[0]) return 0;
                else return 1;
            }
            if (nums[mid] < target && target < nums[mid+1]) return mid+1;
            else {
                if (target < nums[mid]) right = mid;
                else left = mid;
                mid = (left + right) / 2;
            }
        }
        return mid;
    }
};
