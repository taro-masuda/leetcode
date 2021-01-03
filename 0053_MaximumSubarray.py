class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return -2147483648
        elif len(nums) == 1: return nums[0]
        
        max_sum = nums[0]
        previous_sum = nums[0]
        for num in nums[1:]:
            max_sum = max(max_sum, previous_sum, previous_sum + num, num)
            previous_sum = max(previous_sum + num, num)
        return max_sum
