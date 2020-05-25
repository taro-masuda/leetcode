class Solution {
public:
    int trailingZeroes(int n) {
        int out = 0;
        while (n / 5 > 0) {
            out += n / 5;
            n /= 5;
        }
        return out;
    }
};
