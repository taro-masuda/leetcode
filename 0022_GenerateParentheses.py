class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        if n == 0:
            return [""]
        for i in range(2 **(2*n)):
            s = bin(i).replace('0b','').zfill(2*n)
            candidate = ''
            opened = 0
            #print(s)
            for c in s:
                if c == '1':
                    candidate += '('
                    opened += 1
                else:
                    opened -= 1
                    candidate += ')'
                if opened < 0:
                    break
            if opened == 0:
                output.append(candidate)
        
        return output
