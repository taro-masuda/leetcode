class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i_s = 0
        i_t = 0
        n_t = len(t)
        n_s = len(s)
        while i_t < n_t and i_s < n_s:
            if s[i_s] == t[i_t]:
                i_s += 1
            i_t += 1        
        if i_s == n_s:
            return True
        else:
            return False
