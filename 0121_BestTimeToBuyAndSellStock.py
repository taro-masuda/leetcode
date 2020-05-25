import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = sys.maxsize
        
        for i in prices:
            min_val = min(min_val, i)
            max_profit = max(max_profit, i - min_val)
            
        return max_profit
