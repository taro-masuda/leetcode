class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        complement = {}
        out = []
        for i,n in enumerate(nums):
            complement[target-n] = i
        for i,n in enumerate(nums):
            idx = complement.get(n, None)
            if idx != None and idx != i:
                out.append([nums[idx], nums[i]])
                
        return out
                
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        
        out = []
        
        if set(nums) == {0}:
            return [[0,0,0]]
        
        i = 0
        while len(nums) >= 3:
            l_twosum = self.twoSum(nums[1:], -nums[0])
            if l_twosum != None:
                for l in l_twosum:
                    l.append(nums[0])
                    out.append(l)
            nums.pop(0)
        for i,l in enumerate(out):
            out[i] = sorted(l)
        out = list(map(list, set(map(tuple, out))))
        return out
