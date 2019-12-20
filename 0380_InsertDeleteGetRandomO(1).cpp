class RandomizedSet {
private:
    std::random_device rnd;
    std::unordered_map<int, int> mp;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        auto i = mp.find(val);
        if(i == mp.end()){
            mp[val] = val;
            return true;
        } else return false;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        auto i = mp.find(val);
        if(i != mp.end()){
            mp.erase(i);
            return true;
        } else return false;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        auto iter = mp.begin();
        iter = std::next(iter, rnd() % mp.size());
        return iter->first;
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
