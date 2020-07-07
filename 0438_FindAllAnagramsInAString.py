class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        P = len(p)
        S = len(s)
        if P == 0 or S == 0 or S < P:
            return []
        l_p = [0]*26
        l_s = [0]*26
        for i in range(P):
            l_p[ord(p[i])-97] += 1
            l_s[ord(s[i])-97] += 1
        ans = []
        for i in range(S-P+1):
            if l_p == l_s:
                ans.append(i)
            l_s[ord(s[i])-97] -= 1
            if i < S-P:
                l_s[ord(s[P+i])-97] += 1
        return ans
