class Solution {
public:
    int totalFruit(vector<int>& tree) {
        int maxval = 0;
        for (int i = 0; i < tree.size(); i++) {
            if (maxval >= tree.size() - i) break;
            unordered_map<int, int> umap; 
            int val = 0;
            for (int j = i; j < tree.size(); j++) {
                if (umap.find(tree[j]) == umap.end()) {
                    umap[tree[j]] = 0;
                    if (umap.size() == 3) break;
                    else val++;
                } else {
                    umap[tree[j]]++;
                    val++;
                }
            }
            if(maxval < val) maxval = val;
        }
        return maxval;
    }
};
