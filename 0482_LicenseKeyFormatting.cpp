class Solution {
public:
    string licenseKeyFormatting(string S, int K) {
        vector<char> v;
        for (int i = 0; i < S.size(); i++){
            if (S[i] != '-') v.push_back(toupper(S[i]));
        }
        int group_size = 0;
        string out = "";
        for (int i = v.size()-1; i >= 0; i--) {
            if (group_size == K) {
                group_size = 0;
                out += "-";
            }
            out += v[i];
            group_size++;
        }
        
        reverse(out.begin(), out.end());
        return out;
    }
};
