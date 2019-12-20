class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        vector<int> maxnum = {nums[0]};
        vector<int> minimum = {nums[0]};
        for(int i = 1; i < nums.size(); i++){
            maxnum.push_back(max(max(maxnum[i-1]*nums[i], nums[i]), minimum[i-1]*nums[i]));
            minimum.push_back(min(min(minimum[i-1]*nums[i], nums[i]), maxnum[i-1]*nums[i]));
        }
        vector<int>::iterator iter = max_element(maxnum.begin(), maxnum.end());
        return *iter;
    }
};
