class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return min(nums[0], nums[1])
        left = 0
        right = n
        while left < right:
            mid = int((left + right) / 2)
            if mid + 1 < n:
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1]
                elif nums[left] < nums[mid]:
                    left = mid
                else:
                    right = mid
            else:
                return nums[0]
