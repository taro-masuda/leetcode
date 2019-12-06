class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        scores = [0] * len(nums)
    
        scores[0] = nums[0]
        scores[1] = nums[1]
        for i in range(2, len(nums)):
            if i > 2:
                m = max(scores[:i-2+1])
            else:
                m = scores[0]
            scores[i] = max(m + nums[i], scores[i-1])
            
        return scores[-1]
