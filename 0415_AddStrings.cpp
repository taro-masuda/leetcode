class Solution {
public:
    string addStrings(string num1, string num2) {
        int M = num1.size();
        int N = num2.size();
        stack<char> s;
        int countup = 0;
        int m = M-1; int n = N-1;
        while (m >= 0 || n >= 0) {
            int n1 = 0;
            if (m >= 0) n1 = (int)(num1[m] - '0');
            int n2 = 0;
            if (n >= 0) n2 = (int)(num2[n] - '0');
            int sum = n1 + n2 + countup;
            countup = sum / 10;
            s.push((char)(sum % 10 + 48));
            m--; n--;
        }
        if (countup >= 1) s.push((char)(countup + 48));
        string out = "";
        while (!s.empty()) {out += s.top(); s.pop();}
        return out;
    }
};
