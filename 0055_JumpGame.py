class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        maxReachedPoint = 0
        for i,n in enumerate(nums):
            if i > maxReachedPoint:
                pass
            else:
                maxReachedPoint = max(min(i+nums[i], N-1), maxReachedPoint)
        return maxReachedPoint == N-1
