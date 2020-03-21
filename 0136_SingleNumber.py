class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
                
        for num, cnt in d.items():
            if cnt == 1:
                return num
