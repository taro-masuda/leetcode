class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = []
        for n in nums:
            complement.append(target - n) 
        for i,n in enumerate(nums):
            try:
                idx = complement.index(n)
            except ValueError:
                idx = None
            if idx != None and idx != i:
                return [idx, i]
