class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        bits = 0
        out = []
        while bits < 2 ** len(nums):
            l = []
            str_bits = bin(bits).replace('0b', '').zfill(len(nums))
            for i,s in enumerate(str_bits):
                if s == '1':
                    l.append(nums[i])
            out.append(l)
            bits += 1
            
        out = list(map(list, set(map(tuple, out))))
        return out
