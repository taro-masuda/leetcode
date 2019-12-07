class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return 0;
        if (nums.size() == 2){
            if (nums[0] < nums[1]) return 1;
            else return 0;
        }
        int out;
        for (int i = 0; i < nums.size(); i++){
            if (i == 0){
                if (nums[i] > nums[i+1]) return i;
            } else if (i == nums.size()-1){
                if (nums[i] > nums[i-1]) return i;
            } else if (nums[i] > nums[i-1] && nums[i] > nums[i+1]){
                out = i;
                return out;
            }
        }
        return out;
    }
};
