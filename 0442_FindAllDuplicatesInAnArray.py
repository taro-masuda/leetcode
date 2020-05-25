class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        candidates = [x for x in range(1,n+1)]
        for num in nums:
            if candidates[num-1] == num:
                candidates[num-1] = 0
            else:
                candidates[num-1] = num*2
        cur_num = 1
        idx = 0
        while idx < len(candidates):
            if candidates[idx] != 2*cur_num:
                candidates.pop(idx)
            else:
                candidates[idx] = cur_num
                idx += 1
            cur_num += 1
        return candidates
