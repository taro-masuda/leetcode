class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = int(len(nums) / 2)
        right = min(int(len(nums) / 2) + 1, len(nums)-1)
        leftstart = 0
        leftend = len(nums)
        rightstart = 0
        rightend = len(nums)-1
        
        while left <= right:
            if left == right:
                if nums[left] != target:
                    return [-1,-1]
                else:
                    return [left,right]
            if nums[left-1] < target and nums[left] == target and nums[right+1] > target and nums[right] == target:
                return [left, right]
            else:
                if nums[left] < target:
                    leftstart = left
                elif nums[left] > target:
                    leftend = left
                elif nums[left-1] != target:
                    leftstart = left
                left = int((leftstart+leftend) / 2)
                
                if nums[right] > target:
                    rightend = right
                elif nums[right] < target:
                    rightstart = right
                elif nums[right+1] != target:
                    rightend = right
                right = int((rightstart+rightend) / 2)
            
            print(left, right)
        return [-1,-1]
