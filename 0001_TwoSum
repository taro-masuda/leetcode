class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_outer_loop = 0
        idx_inner_loop = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and not i == j:
                    return [i, j]
