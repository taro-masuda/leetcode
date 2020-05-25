class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t t = 0;
        for(uint32_t mask = 1; mask != 0; mask<<=1) {
            t <<= 1;
            if( (n & mask) != 0 ){   // nの当該ビットが立っていれば
                t |= 1;    // 結果のビットを立てる
            }
        }
        n = t;
        return n;
    }
};
