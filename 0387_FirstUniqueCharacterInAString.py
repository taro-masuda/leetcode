class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i,c in enumerate(s):
            if not c in d:
                d[c] = [i,1]
            else:
                d[c][1] += 1
        for c in d:
            if d[c][1] == 1:
                return d[c][0]
        return -1
