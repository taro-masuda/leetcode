import copy

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set = list(set(nums))
        nums_set_count = []
        for num in nums_set:
            nums_set_count.append(nums.count(num))
        
        nums_set_count_orig = copy.copy(nums_set_count)
        nums_set_count.sort(reverse=True)
        
        out = []
        print(nums_set)
        for idx in range(k):
            idx_k = nums_set_count_orig.index(nums_set_count[idx])
            out.append(nums_set[idx_k])
            nums_set_count_orig[idx_k] = -1
        
        return out
