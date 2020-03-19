class Solution:
    def __init__(self):
        self.dic = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        if amount in self.dic:
            return self.dic[amount]
        cnt = amount+1
        
        for c in coins:
            if amount-c == 0:
                cnt = 1
                break
            num = self.coinChange(coins, amount-c)
            if num > 0:
                if num+1 < cnt:
                    cnt = num+1
        if cnt == amount+1:
            cnt = -1
        self.dic[amount] = cnt
        return cnt
