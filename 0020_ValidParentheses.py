class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        
        for c in list(s):
            if c == '(': 
                l.append(0)
            elif c == '[':
                l.append(1)
            elif c == '{':
                l.append(2)
            elif len(l) == 0:
                return False
            elif c == ')':
                if l.pop(-1) != 0:
                    return False
            elif c == ']':
                if l.pop(-1) != 1:
                    return False
            elif c == '}':
                if l.pop(-1) != 2:
                    return False
                
        if len(l) != 0:
            return False
        else:
            return True
