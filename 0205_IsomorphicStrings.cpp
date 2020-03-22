class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char,int> umap;
        unordered_map<char,char> umap_t;
        unordered_map<char,int> umap_tcnt;
        int N = s.size();
        for (int i = 0; i < N; i++) {
            if (umap.find(s[i]) == umap.end()) umap[s[i]] = 1;
            else umap[s[i]]++;
            if (umap_t.find(t[i]) == umap_t.end()) {
                umap_t[t[i]] = s[i];
                umap_tcnt[umap_t[t[i]]] = 1;
            }
            else if (umap_t[t[i]] != s[i]) return false;
            else umap_tcnt[umap_t[t[i]]]++;
            if (umap[s[i]] != umap_tcnt[umap_t[t[i]]]) return false;
        }
        return true;
    }
};
