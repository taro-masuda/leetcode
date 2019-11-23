import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        for i in range(2,int(math.sqrt(num))+1):
            if i*i == num:
                return True
        return False
