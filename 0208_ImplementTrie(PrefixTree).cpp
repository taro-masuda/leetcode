class Trie {
private:
    vector<string> v;
public:
    /** Initialize your data structure here. */
    Trie() {
        
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        v.push_back(word);
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        for (int i = 0; i < v.size(); i++){
            if(v[i] == word) return true;
        }
        return false;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        for (int i = 0; i < v.size(); i++){
            if(v[i].size() >= prefix.size() && equal(begin(prefix), end(prefix), begin(v[i]))){
                return true;
            }
        }
        return false;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
