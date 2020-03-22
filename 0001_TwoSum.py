class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i,n in enumerate(nums):
            complement[target-n] = i
        for i,n in enumerate(nums):
            if n in complement:
                if complement[n] != i:
                    return [i, complement[n]]
