class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []; t = []
        for i in range(len(S)):
            if S[i] == "#":
                if len(s) > 0:
                    s.pop(-1)
            else:
                s.append(S[i])
        for i in range(len(T)):
            if T[i] == "#":
                if len(t) > 0:
                    t.pop(-1)
            else:
                t.append(T[i])
        return s == t
