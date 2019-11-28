class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = []
        #print(nums)
        out = []
        for n in nums:
            complement.append(target - n) 
        for i,n in enumerate(nums):
            try:
                idx = complement.index(n)
            except ValueError:
                idx = None
            #print(complement)
            #print(n, idx, i)
            if idx != None and idx != i:
                out.append([nums[idx], nums[i], -target])
        return out
                
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        
        out = []
        print('a')
        
        i = 0
        #for i,n in enumerate(nums):
        while len(nums) >= 3:
            if nums[0] > 0:
                break
            l_twosum = self.twoSum(nums[1:], -nums[0])
            if l_twosum != None:
                #print(l_twosum, i, n)
                out.extend(l_twosum)
            nums.pop(0)
            
        print('b')
        for i,l in enumerate(out):
            out[i] = sorted(l)
        print('c')
        out = list(map(list, set(map(tuple, out))))
        return out
