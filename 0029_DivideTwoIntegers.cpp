class Solution {
public:
    int divide(int dividend, int divisor) {
        int dividedCount = 0;
        
        if (dividend == - pow(2,31) && divisor == -1) return pow(2,31) - 1;
        else if (dividend == - pow(2,31) && divisor > 0) {
            dividend += divisor;
            dividedCount++;
        } else if (dividend == - pow(2,31) && divisor < 0) {
            dividend -= divisor;
            dividedCount++;
        }
        
        if (dividend > 0 && divisor > 0) {
            while (dividend >= divisor) {
                dividend -= divisor;
                dividedCount++;
            }
            return dividedCount;
        } else if (dividend > 0 && divisor < 0) {
            while (-dividend <= divisor) {
                dividend += divisor;
                dividedCount++;
            }
            return -dividedCount;
        } else if (dividend < 0 && divisor > 0) {
            while (-dividend >= divisor) {
                dividend += divisor;
                dividedCount++;
            }
            return -dividedCount;
        } else if (dividend < 0 && divisor < 0) {
            while (-dividend >= -divisor) {
                dividend -= divisor;
                dividedCount++;
            }
            return dividedCount;
        } else return 0; // dividend == 0 && divisor != 0
    }
};
