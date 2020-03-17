class Solution:
    def binarySearch(self, l, target):
        N = len(l)
        if N == 1:
            return target == l[0]
        left = 0
        right = N
        mid_history = None
        while right-left >= 1:
            mid = int((right + left) / 2)
            if mid_history == mid:
                break
            if l[mid] == target:
                return True
            elif l[mid] > target:
                right = mid
            else:
                left = mid
            mid_history = mid
        return False
    
    def mergeSort(self, l1, l2):
        l = []
        i1 = 0
        i2 = 0
        while i1 < len(l1) and i2 < len(l2):
            if l1[i1] <= l2[i2]:
                l.append(l1[i1])
                i1 += 1
            else:
                l.append(l2[i2])
                i2 += 1
        if i1 < len(l1):
            while i1 < len(l1):
                l.append(l1[i1])
                i1 += 1
        else:
            while i2 < len(l2):
                l.append(l2[i2])
                i2 += 1
        return l
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        
        # merge sort
        l = matrix[0]
        for i in range(len(matrix)-1):
            l_new = self.mergeSort(l, matrix[i+1])
            #print(l_new)
            l = l_new
        print(l)
        return self.binarySearch(l, target)
