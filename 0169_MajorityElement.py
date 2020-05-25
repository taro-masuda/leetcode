class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        idx = 0
        while idx < n:
            if nums.count(nums[idx]) >= int(n/2)+1:
                return nums[idx]
            else:
                nums = [i for i in nums if i != nums[idx]]
