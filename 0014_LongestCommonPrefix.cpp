class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) return "";
        string lcp = strs[0];
        for (int i = 1; i < strs.size(); i++){
            while(!(strs[i].size() >= lcp.size() && equal(begin(lcp), std::end(lcp), std::begin(strs[i])))){
                lcp.pop_back();
            }
        }
        
        return lcp;
    }
};
