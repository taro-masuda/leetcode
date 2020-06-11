import numpy as np

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        return list(np.dot(np.array(A), np.array(B)))
