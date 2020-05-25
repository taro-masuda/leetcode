class Solution:
    def validPalindrome_nodelete(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        cnt_del = 0
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        cnt_del = 0
        isPal = True
        while left < right:
            if s[left] != s[right]:
                if (self.validPalindrome_nodelete(s[left+1:right+1]) or  
                    self.validPalindrome_nodelete(s[left:right])):
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return isPal
