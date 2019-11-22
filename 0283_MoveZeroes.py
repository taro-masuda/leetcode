class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = nums.count(0)
        idx = 0
        while idx < len(nums)-count_zero:
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
            else:
                idx += 1
