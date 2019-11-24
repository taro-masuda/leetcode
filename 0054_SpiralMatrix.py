class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        out = []
        if n == 1:
            for i in range(m):
                out.append(matrix[i][0])
            return out
        if m == 1:
            for i in range(n):
                out.append(matrix[0][i])
            return out

        row_bgn = 0
        col_bgn = 0
        col_end = n-1
        row_end = m-1
        
        cnt = 0
        while len(out) < m*n:
            if cnt % 4 == 0:
                if col_bgn == col_end:
                    out.append(matrix[row_bgn][col_bgn]) # toward right
                else:
                    out.extend(matrix[row_bgn][col_bgn:col_end+1]) # toward right
                row_bgn += 1
            elif cnt % 4 == 1:
                for i in range(row_bgn, row_end+1):
                    out.append(matrix[i][col_end]) # toward bottom
                col_end -= 1
            elif cnt % 4 == 2:            
                if col_bgn == col_end:
                    out.append(matrix[row_end][col_bgn]) # toward left
                else:
                    for i in range(col_end,col_bgn-1,-1):
                        out.append(matrix[row_end][i]) # toward left 
                row_end -= 1
            else:
                for i in range(row_end, row_bgn-1, -1):
                    out.append(matrix[i][col_bgn]) # toward up
                col_bgn += 1    
                
            cnt += 1
            
        return out
