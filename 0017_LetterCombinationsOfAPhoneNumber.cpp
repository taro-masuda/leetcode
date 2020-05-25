class Solution {
private:
    vector<vector<char>> num2abc = {{'\0','\0','\0','\0'},{'\0','\0','\0','\0'},
                     {'a', 'b', 'c','\0'}, {'d', 'e', 'f','\0'},
                      {'g', 'h', 'i','\0'}, {'j', 'k', 'l','\0'},
                      {'m', 'n', 'o','\0'}, {'p', 'q', 'r', 's'},
                      {'t', 'u', 'v','\0'}, {'w', 'x', 'y', 'z'}};
public:
    vector<string> addLetters(vector<string> in, const char* s){
        vector<string> out;
        int s_num = *s - '0';
        if (in.size() == 0) {
            for (int j = 0; j < num2abc[s_num].size(); j++) {
                if (num2abc[s_num][j] == '\0') break;
                string toPush = string(1, num2abc[s_num][j]);
                out.push_back(toPush);
            }
        } else {
            for (int i = 0; i < in.size(); i++) {
                for (int j = 0; j < num2abc[s_num].size(); j++) {
                    if (num2abc[s_num][j] == '\0') break;
                    string toPush = string(1, num2abc[s_num][j]);
                    out.push_back(in[i] + toPush);
                }
            }
        }
        return out;
    }
    vector<string> letterCombinations(string digits) {
        vector<string> v = {};
        for (int i = 0; i < digits.size(); i++){
            char a = digits[i];
            v = addLetters(v, &a);
        }
        return v;
    }
};
