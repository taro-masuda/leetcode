class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        elif len(s) == 2:
            if s[0] == s[1]: return s
            else: return s[0]

        N = len(s)
        dic = {}
        maxstr = ""
        for i,c in enumerate(s):
            # even palindromes
            if i == N-1: continue
            left = i; right = i+1
            if s[i] != s[i+1]: continue
            while True:
                if left-1 < 0 or right+1 >= N: break
                elif s[left-1] == s[right+1]: left -= 1; right += 1
                else:
                    break
            if len(maxstr) < right - left + 1:
                maxstr = s[left:right+1]
        for i,c in enumerate(s): 
            # odd palindromes
            if i == 0 or i == N-1: continue
            left = i; right = i
            while True:
                if left-1 < 0 or right+1 >= N: break
                elif s[left-1] == s[right+1]: left -= 1; right += 1
                else: break
            if len(maxstr) < right - left + 1:
                maxstr = s[left:right+1]
                
        return maxstr
