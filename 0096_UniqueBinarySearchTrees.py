class Solution:
    def __init__(self):
        self.dic = {}
    def numTrees(self, n: int) -> int:
        if n in self.dic:
            return self.dic[n]
        if n <= 2:
            self.dic[n] = max(n, 1)
            return self.dic[n]
        else:
            ans = 0
            for i in range(n):
                ans += self.numTrees(i) * self.numTrees(n-i-1)
            self.dic[n] = ans
            return ans
