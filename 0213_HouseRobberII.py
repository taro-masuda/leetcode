class Solution:
    def __init__(self):
        self.dic_no_circle = {}
    
    def rob_no_circle(self, nums: List[int], start, end) -> int:
        n = len(nums)
        if (start,end) in self.dic_no_circle:
            return self.dic_no_circle[start,end]
        if n == 0:
            return 0
        if n == 1:
            self.dic_no_circle[start,end] = nums[0]
            return nums[0]
        if n == 2:
            self.dic_no_circle[start,end] = max(nums[0], nums[1])
            return self.dic_no_circle[start,end]
        ans = max(self.rob_no_circle(nums[:-2], start, end-2)+nums[-1],self.rob_no_circle(nums[:-1], start, end-1))
        self.dic_no_circle[start,end] = ans
        return ans
        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return self.rob_no_circle(nums, 0, n)
        if n == 3:
            return max(nums[0], nums[1], nums[2])
        # if the robber robs at the last (n-1 th) house, you cannot rob from index 0 and n-2.
        profit = self.rob_no_circle(nums[1:-2], 1, n-2) + nums[-1]
        # if the robber robs as the first (0 th) house, you cannot rob from index 1 and n-1.
        profit = max(profit, self.rob_no_circle(nums[2:-1], 2, n-1) + nums[0])
        # what if we choose neither index 0 nor index n-1?
        profit = max(profit, self.rob_no_circle(nums[1:-1], 1, n-1))
        
        return profit
