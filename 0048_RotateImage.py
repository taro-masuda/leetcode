class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        a = []
        for row in range(n):
            a.extend(matrix[row])
        for row in range(n):
            matrix[row] = a[n*(n-1)+row::-n]
