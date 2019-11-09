class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        idx = 0
        nums.sort()
        while idx < len(nums):
            if nums.count(nums[idx]) == 1:
                return nums[idx]
            else:
                nums.pop(idx)
                nums.pop(idx)
