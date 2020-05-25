class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> v;
        vector<int> out;
        for (int i = 0; i < nums.size(); i++){
            v.push_back(0);
        }
        for (int i = 0; i < nums.size(); i++){
            v[nums[i]-1]++;
        }
        for (int i = 0; i < nums.size(); i++){
            if(v[i] == 0) out.push_back(i+1); 
        }
        
        return out;
    }
};
