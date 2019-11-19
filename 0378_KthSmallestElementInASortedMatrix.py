import numpy as np

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        minimum_list = []
        
        for m in matrix:
            minimum_list.append(m.pop(0))
        
        i = 1
        while i <= k:
            idx = np.argmin(minimum_list)
            if i == k:
                return min(minimum_list) #matrix[idx].pop(0)
            else:
                if len(matrix[idx]) == 0:
                    minimum_list[idx] = np.inf
                else:
                    minimum_list[idx] = matrix[idx].pop(0)
                i += 1            
