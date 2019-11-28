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
        
        out = []
        
        for i,n in enumerate(nums):
            
            if i == 0:
                #print(nums[i+1:], n)
                l_twosum = self.twoSum(nums[i+1:], -n)
            elif i == len(nums)-1:
                #print(nums[:i], n)
                l_twosum = self.twoSum(nums[:i], -n)
            else:
                #print(nums[:i] + nums[i+1:], n)
                l_twosum = self.twoSum(nums[:i] + nums[i+1:], -n)
            if l_twosum != None:
                #print(l_twosum, i, n)
                out.extend(l_twosum)
        
        for i,l in enumerate(out):
            out[i] = sorted(l)
        print(out)
        out = list(map(list, set(map(tuple, out))))
        return out
