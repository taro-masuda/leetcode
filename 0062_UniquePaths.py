class Solution:
    def permutation(self,n: int) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            return n*self.permutation(n-1)
    def uniquePaths(self, m: int, n: int) -> int:
        return int(self.permutation(m+n-2) / (self.permutation(m-1)*self.permutation(n-1)))
