class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -2147483648
        if len(nums) == 1:
            return nums[0]
        previousSum = nums[0]
        maxSum = nums[0]
        for n in nums[1:]:
            maxSum = max(maxSum, previousSum, previousSum + n, n)
            previousSum = max(previousSum + n, n)
            
        return maxSum
