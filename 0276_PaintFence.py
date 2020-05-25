class Solution:
    def __init__(self):
        self.con = {}
        self.non = {}
    def numWays(self, n: int, k: int) -> int:
        if n in self.con and n in self.non:
            return self.con[n] + self.non[n]
        
        self.con[0] = 0
        self.non[0] = 0
        if n == 0:
            return 0
        
        self.con[1] = 0
        self.non[1] = k
        if n == 1:
            return k
        
        i = 2
        while i <= n:
            self.con[i] = self.non[i-1]
            self.non[i] = (k-1) * self.con[i-1] + (k-1) * self.non[i-1]
            i += 1
        
        return self.con[n] + self.non[n]
