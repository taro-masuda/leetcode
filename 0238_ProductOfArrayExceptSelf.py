class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        mul = 1
        if nums.count(0) == 1:
            for i, num in enumerate(nums):
                if num != 0:
                    mul *= num
                out[i] = 0
            out[nums.index(0)] = mul
        elif nums.count(0) > 1:
            return [0] * len(nums)
        else:
            for i, num in enumerate(nums):
                out[i] =  num**-1
                mul *= num
            for i, num in enumerate(nums):
                out[i] = round(out[i] * mul)
    
        return out
