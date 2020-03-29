class Solution {
public:
    string minRemoveToMakeValid(string s) {
        queue<int> open;
        queue<int> todelete;
        int N = s.size();
        for (int i = 0; i < N; i++){
            if (s[i] == '(' ) {
                open.push(i);
            } else if (s[i] == ')') {
                if (open.empty()) todelete.push(i);
                else open.pop();
            }
        }
        string out = "";
        for (int i = 0; i < N; i++) {
            if (todelete.front() == i) {
                todelete.pop();
            } else if (open.front() == i) {
                open.pop();
            } else out += s[i];
        }
        return out;
    }
};
