class Solution {
public:
    string getHint(string secret, string guess) {
        int bulls[10] = {0}, cows[10] = {0};
        
        unordered_map<char, int> umap_g;
        unordered_map<char, int> umap_s;
        
        for (int i = 0; i < secret.size(); i++) {
            if (secret[i] == guess[i]) {
                bulls[(int)(guess[i] - '0')]++;
                continue;
            }
            if (umap_g.find(guess[i]) == umap_g.end()) {
                umap_g[guess[i]] = 1;
            } else umap_g[guess[i]]++;
            if (umap_s.find(secret[i]) == umap_s.end()) {
                umap_s[secret[i]] = 1;
            } else umap_s[secret[i]]++;
        }
        int A = 0, B = 0;
        for (int num = 0; num <= 9; num++) {
            A += bulls[num];
            B += min(umap_s[(char)(num+48)], umap_g[(char)(num+48)]);
        }
        return to_string(A) + "A" + to_string(B) + "B";
    }
};
