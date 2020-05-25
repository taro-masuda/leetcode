class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        # check whether all the values can be the same
        can_be_done = [True,True,True,True,True,True]
        for i in range(6):
            for idx in range(len(A)):
                if A[idx] != i+1 and B[idx] != i+1:
                    can_be_done[i] = False
                    break
        
        counter_A = [] # if we set value i(0~5) for all the element of A, how many rotate is needed?
        counter_B = [] # if we set value i(0~5) for all the element of B, how many rotate is needed?
        
        for i in range(6):
            if can_be_done[i]:
                counter_A.append(0)
                counter_B.append(0)
                for idx in range(len(A)):
                    if A[idx] == i+1 and B[idx] != i+1:
                        counter_B[i] += 1
                    if A[idx] != i+1 and B[idx] == i+1:
                        counter_A[i] += 1
                        
            else:
                counter_A.append(10000)
                counter_B.append(10000)
                
        if sum(can_be_done) == 0:
            return -1
        else:
            return min(min(counter_A), min(counter_B))
