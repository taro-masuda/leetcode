class Solution {
public:
    int divide(int dividend, int divisor) {
        int sign;
        if (dividend > 0) {
            dividend = - std::abs(dividend);
            sign = 1;
        }else {sign = -1;}
        if (divisor > 0) {
            divisor = - std::abs(divisor);
            if(sign == -1) sign = -1;
            else sign = 1;
        }else {
            if (sign == -1) sign = 1;
            else sign = -1;
        }
        int out = 0;
        while (dividend <= divisor){
            dividend -= divisor;
            out += 1;
        }
        if (sign == -1) return -out;
        else return out;
    }
};
