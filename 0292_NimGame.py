class Solution:
    def canWinNim(self, n: int) -> bool:
        if n == 0:
            return False
        if n % 4 == 0:
            return False
        else:
            return True
