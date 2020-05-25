class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        else:
            l = list(self.countAndSay(n-1))
            
            out = ''
            consecutive = 1
            for i,c in enumerate(l):
                if i == len(l) - 1:
                    out += str(consecutive) + l[i]
                elif l[i] == l[i+1]:
                    consecutive += 1
                else:
                    out += str(consecutive) + l[i]
                    consecutive = 1
            
            return out
