class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size() == 0) return -1;
        else if (nums.size() == 1) {
            if (nums[0] == target) return 0;
            else return -1;
        } else if (nums.size() == 2) {
            if (nums[0] == target) return 0;
            else if (nums[1] == target) return 1;
            else return -1;
        } else if (nums.size() == 3) {
            if (nums[0] == target) return 0;
            else if (nums[1] == target) return 1;
            else if (nums[2] == target) return 2;
            else return -1;
        }
        int leftstart = 0;
        int leftend, rightstart;
        int rightend = nums.size();
        
        for (int i = 0; i < nums.size()-1; i++) {
            if (nums[i] > nums[i+1]) {
                leftend = i+1;
                rightstart = i+1;
                break;
            }
            if (i == nums.size()-2) {
                leftend = nums.size();
                rightstart = 0;
            }
        }
        
        int start, end;
        if (target >= nums[leftstart] && target <= nums[leftend-1]) {
            start = leftstart;
            end = leftend;
        } else if (target >= nums[rightstart] && target <= nums[rightend-1]) {
            start = rightstart;
            end = rightend;
        }
        
        while (start < end) {
            int half = (start + end) / 2;
            if (nums[half] == target) return half;
            else if (nums[half] < target) start = half + 1;
            else end = half;
        }
        return -1;
    }
};
