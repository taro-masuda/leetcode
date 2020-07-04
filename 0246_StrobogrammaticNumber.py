class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        n = len(num)
        if n % 2 == 1:
            if num[int(n/2)] == '8' or num[int(n/2)] == '1' or num[int(n/2)] == '0':
                pass
            else:
                return False
        left = 0; right = n-1
        while left < right:
            if (num[left] == '6' and num[right] == '9') or (num[left] == '9' and num[right] == '6'):
                pass
            elif (num[left] == '1' and num[right] == '1'):
                pass
            elif (num[left] == '8' and num[right] == '8'):
                pass
            elif (num[left] == '0' and num[right] == '0'):
                pass
            else:
                return False
            left += 1; right -= 1
        return True
