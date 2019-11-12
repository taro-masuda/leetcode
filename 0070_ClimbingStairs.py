class Solution:
    
    def memoize(f):
        memo = {}
        def helper(solution,x):
            if x not in memo:            
                memo[x] = f(solution,x)
            return memo[x]
        return helper
    
    @memoize
    def climbStairs(self, n: int) -> int:
        if n > 2:
                return self.climbStairs(n-1) + self.climbStairs(n-2)
        else:
            return n
