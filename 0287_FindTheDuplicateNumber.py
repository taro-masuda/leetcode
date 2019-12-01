class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                return nums[i]
            else:
                i += 1
