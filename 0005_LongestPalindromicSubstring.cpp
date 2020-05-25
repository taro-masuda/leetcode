struct Section {
    int l;
    int r;
};

class Solution {
public:
    bool isPalindromeTwo(char c1, char c2){
        return c1 == c2;
    }
    
    string longestPalindrome(string s) {
        // two substring check
        int N = s.size();
        if (N==1) return s;
        if (N==2) {
            if (s[0] != s[1]) return s.substr(0,1);
        }
        vector<struct Section> sec;
        
        for (int i = 0; i+1 < N; i++) {
            struct Section si;
            si.l = i;
            si.r = i+1 + 1;
            if (isPalindromeTwo(s[i], s[i+1])) sec.push_back(si); 
        }
        for (int i = 0; i+2 < N; i++) {
            struct Section si;
            si.l = i;
            si.r = i+2 + 1;
            if (isPalindromeTwo(s[i], s[i+2])) sec.push_back(si);
        }
        
        string longest = "";
        while (sec.size() > 0) {
            struct Section si;
            si = sec.back(); sec.pop_back();
            while (si.l > 0 && si.r <= N){
                if (isPalindromeTwo(s[si.l-1], s[si.r+1-1])) {si.l--; si.r++;}
                else break;
            }
            string substring = s.substr(si.l,si.r-si.l);
            if (substring.size() > longest.size()) longest = substring;
        }
        if (longest == "") return s.substr(0,1);
        return longest;
    }
};
