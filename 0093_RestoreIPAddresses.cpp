class Solution {
public:
    string substringToAddress(string A) {
        if (A[0] == '0' && A.size() > 1) return "";
        string::size_type sz;   // alias of size_t
        int i_dec = stoi(A,&sz);    
        if (!(i_dec >= 0 && i_dec <= 255)) return "";
        else return A;
    }
    
    vector<string> restoreIpAddresses(string s) {
        int N = s.size();
        vector<string> ans;
        if (N > 12) return ans;
        for (int i = 1; i < N-2; i++) {
            for (int j = i+1; j < N-1; j++) {
                for (int k = j+1; k < N; k++) {
                    if (N-k > 3 || N-k < 0) continue;
                    string candidate = "";
                    string A = s.substr(0,i);
                    string subAdd = substringToAddress(A);
                    if (subAdd == "") continue;
                    candidate += subAdd + ".";
                    string B = s.substr(i,j-i);
                    subAdd = substringToAddress(B);
                    if (subAdd == "") continue;
                    candidate += subAdd + ".";
                    string C = s.substr(j,k-j);
                    subAdd = substringToAddress(C);
                    if (subAdd == "") continue;
                    candidate += subAdd + ".";
                    string D = s.substr(k,N-k);
                    subAdd = substringToAddress(D);
                    if (subAdd == "") continue;
                    candidate += subAdd;
                    ans.push_back(candidate);
                }
            }
        }
        return ans;
    }
};
