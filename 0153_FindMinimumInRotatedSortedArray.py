class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return min(nums[0], nums[1])
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]
