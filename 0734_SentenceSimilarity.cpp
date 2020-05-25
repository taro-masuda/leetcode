class Solution {
public:
    bool areSentencesSimilar(vector<string>& words1, vector<string>& words2, vector<vector<string>>& pairs) {
        int N = words1.size();
        if (N != words2.size()) return false;
        for (int i = 0; i < N; i++) {
            string w1 = words1[i];
            bool simWordExists = false;
            string w2 = words2[i];
            for (int i1 = 0; i1 < pairs.size(); i1++) {
                if (pairs[i1][0] == w1) {
                    if (pairs[i1][1] == w2) simWordExists = true;
                }
                if (pairs[i1][0] == w2) {
                    if (pairs[i1][1] == w1) simWordExists = true;
                }
            }
            if (w1 == w2) simWordExists = true;
            if (!simWordExists) return false;
        }
        return true;
    }
};
