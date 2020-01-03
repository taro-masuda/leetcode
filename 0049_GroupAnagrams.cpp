class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<string> sort_strs;
        unordered_map<string, int> mp;
        int idx = 0;
        for (int i = 0; i < strs.size(); i++) {
            string s_sort = strs[i];
            sort(s_sort.begin(), s_sort.end());
            sort_strs.push_back(s_sort);
            auto j = mp.find(s_sort);
            if(j == mp.end()) {
                mp[s_sort] = idx; idx++;
            }
        }
        
        vector<vector<string>> out;
        while (out.size() < idx) {
            out.push_back({});
        }
        for (int i = 0; i < strs.size(); i++) {
            out[mp[sort_strs[i]]].push_back(strs[i]);
        }
        
        return out;
    }
};
