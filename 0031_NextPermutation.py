class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        if nums[-2] < nums[-1]:
            nums[-2], nums[-1] = nums[-1], nums[-2]
            return
        ascend = None
        descend = None
        for i, num in enumerate(nums[:-1]):
            if nums[i] < nums[i+1]:
                ascend = i
            if nums[i] > nums[i+1]:
                descend = i
        if ascend is None:
            nums.reverse()
            return
        if descend is None:
            nums[ascend], nums[ascend+1] = nums[ascend+1], nums[ascend]
            return
            
        idx = ascend+1
        while idx < len(nums):
            if nums[idx] <= nums[ascend]:
                idx = max(0, idx-1)
                break
            else:
                idx += 1
        idx = min(idx, len(nums)-1)
        nums[ascend], nums[idx] = nums[idx], nums[ascend]
        nums[ascend+1:] = sorted(nums[ascend+1:])
