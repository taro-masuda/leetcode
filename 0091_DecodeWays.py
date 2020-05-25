class Solution:
    def __init__(self):
        self.dic = {}
    def numDecodings(self, s: str) -> int:
        if s in self.dic:
            return self.dic[s]
        if len(s) == 0:
            return 0
        if (s[0] == '0'):
            return 0
        if len(s) == 1:
            return 1
        elif len(s) == 2:
            if int(s) <= 26:
                if int(s) % 10 != 0: # e.g. 18
                    return 2
                else:
                    return 1 # 10 or 20
            elif int(s) % 10 != 0: # e.g. 72
                return 1
            else: # e.g. 70
                return 0
            
        num2 = int(s[:2])
        future_dec2 = self.numDecodings(s[2:])
        future_dec1 = self.numDecodings(s[1:]) - future_dec2
        if future_dec2 == 0:
            self.dic[s] = future_dec1
        elif num2 <= 26 and num2 % 10 != 0: # e.g. 17
            self.dic[s] = future_dec1 + 2*future_dec2
        elif num2 % 10 != 0: # e.g. 67
            self.dic[s] = future_dec1 + future_dec2
        elif num2 == 10 or num2 == 20:
            self.dic[s] = future_dec2 # e.g. 10, 20
        else:
            self.dic[s] = 0
        return self.dic[s]
