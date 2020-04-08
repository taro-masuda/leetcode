class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> s;
        vector<int> out;
        int N = asteroids.size();
        if (N == 0) return out;
        for (int asteroid : asteroids) s.push(asteroid);
        stack<int> bak;
        while (!s.empty()) {
            int cur = s.top(); s.pop();
            if (s.empty()) {bak.push(cur); break;}
            if (cur < 0 && s.top() > 0) {
                if (s.top() < -cur) {
                    s.pop(); s.push(cur); // positive one exploded
                } else if (s.top() == -cur) s.pop(); // both asteroids exploded
                while (!bak.empty()) {
                    s.push(bak.top()); bak.pop();
                }
            } else {
                bak.push(cur);
            }
        }
        while (!bak.empty()) { out.push_back(bak.top()); bak.pop(); }
        return out;
    }
};
