class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        if N == 0:
            return [-1,-1]
        if N == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        elif N == 2:
            if nums[0] == target:
                if nums[1] == target:
                    return [0,1]
                else:
                    return [0,0]
            elif nums[1] == target:
                return [1,1]
            else:
                return [-1,-1]
        bgn = self.search(nums, target, "start")
        end = self.search(nums, target, "end")
        return [bgn, end]
    
    def search(self, nums, target, start_end):
        N = len(nums)
        left = 0; right = N
        while right - left > 1:
            mid = int((left + right) / 2)
            if start_end == "start":
                if mid == 0 and nums[mid] == target:
                    return mid
                elif nums[mid] == target and nums[mid-1] < target:
                    return mid
            else:
                if mid+1 == N and nums[mid] == target:
                    return mid
                if nums[mid] == target and nums[mid+1] > target:
                    return mid
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                if start_end == "start":
                    right = mid
                else:
                    left = mid
        if nums[left] == target:
            return left
        elif nums[mid] == target and start_end == "end":
            return mid
        else:
            return -1
