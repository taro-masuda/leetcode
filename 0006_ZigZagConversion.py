class Solution:
    def convert(self, s: str, numRows: int) -> str:
        N = len(s)
        idx = 0
        numrow = 0
        strs_rows = []
        
        if N <= numRows or numRows == 1:
            return s
        
        for i in range(numRows):
            strs_rows.append([s[i]])
            idx += 1
            numrow += 1
        mode = 'upward'
        numrow -= 1
        while idx < N:
            if numrow == numRows-1:
                mode = 'upward'
            elif numrow == 0:
                mode = 'downward'
            if mode == 'upward':
                numrow -= 1
            else:
                numrow += 1
            strs_rows[numrow].append(s[idx])
            idx += 1
            
        out = ""
        for i in range(numRows):
            out += "".join(strs_rows[i])
        return out
