class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> vec;
        std::sort(nums.begin(), nums.end());
        nums.erase(std::unique(nums.begin(), nums.end()), nums.end());
        const int N = nums.size();
        for (int i = 0; i < pow(2, N); i++){ //
            string s = std::bitset<N>(i);
            while (s.size() < N) s = "0" + s;
            vector<int> v;
            for (int j = 0; j < nums.size(); v++){
                if(s[j] == 1) v.push_back(nums[j]);
            }
            vec.push_back(v);
            /*int j = i;
            while (j != 0){
                if (j & 1 == 1){
                    
                }
                j >> 1;
            }*/
        }
        
        return vec;
    }
};
