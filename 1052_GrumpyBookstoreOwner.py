class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        num_satisfied = 0
        num_not_satisfied = 0
        l_not_satisfied = []
        for i,customer in enumerate(customers):
            if grumpy[i] == 0:
                num_satisfied += customer
            else:
                num_not_satisfied += customer
            l_not_satisfied.append(num_not_satisfied)
        
        num_changed = 0
        for i in range(len(customers)-X+1):
            if i == 0:
                changed_at_i = l_not_satisfied[X-1]
            else:
                changed_at_i = l_not_satisfied[i+X-1] - l_not_satisfied[i-1]
            num_changed = max(num_changed,changed_at_i)
            
        return num_satisfied + num_changed
