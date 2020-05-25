class Solution(object):
    def __init__(self):
        self.cum_min = []
        self.result = {}
    def maxProfit_n(self, prices, n):
        if n <= 1:
            return 0
        if n == 2:
            return max(0, prices[1]-prices[0])
        # n >= 3:
        if n not in self.result:
            self.result[n] = max(0, self.maxProfit_n(prices, n-2) 
                                 + max(prices[n-1]-prices[n-2],
                                       prices[n-1]-prices[n-3],
                                       prices[n-2]-prices[n-3], 0),
                                prices[n-2]-self.cum_min[n-2], prices[n-1]-self.cum_min[n-2])
        return self.result[n]
            
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        self.cum_min.append(prices[0])
        self.cum_min.append(min(prices[0], prices[1]))
        for i in range(2,len(prices)):
            self.cum_min.append(min(self.cum_min[i-1], prices[i]))
        return self.maxProfit_n(prices, len(prices))
