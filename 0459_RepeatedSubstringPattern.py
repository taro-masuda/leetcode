class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        if N <= 1:
            return False
        elif N == 2:
            return s[0] == s[1]
        for k in range(1, int(N/2)+1):
            if N % k != 0:
                continue
            isRepeated = True
            for i in range(1, int(N/2)+1):
                for j in range(0,N-i+1,k):
                    if s[i-1] != s[i+j-1]:
                        isRepeated = False
                        break
                if not isRepeated:
                    break
            if isRepeated:
                return True
        return isRepeated
