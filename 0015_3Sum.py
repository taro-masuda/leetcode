import bisect

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        while len(nums) >= 2:
            if nums.count(-target-nums[0]) > 0:
                out.append([-target-nums[0], nums[0], target])
            nums.pop(0)
        return out
                
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        
        out = []
        
        i = 0
        while len(nums) >= 3:
            if nums[0] > 0:
                break
            l_twosum = self.twoSum(nums[1:], nums[0])
            if l_twosum != None:
                out.extend(l_twosum)
            nums.pop(0)
            
        for i,l in enumerate(out):
            out[i] = sorted(l)
        out = list(map(list, set(map(tuple, out))))
        return out
