class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        N = len(nums)
        min_len = N+1
        if N == 0:
            return 0
        start = 0
        end = 0
        cur_sum = nums[0]
        while start < N:
            if s == cur_sum:
                min_len = min(min_len, end-start+1)
                if end == N-1:
                    break
                end += 1
                cur_sum += nums[end]
            elif cur_sum < s:
                if end == N-1:
                    break
                end += 1
                cur_sum += nums[end]
            else:
                min_len = min(min_len, end-start+1)
                cur_sum -= nums[start]
                start += 1
                if start == N:
                    break
                if start > end:
                    start = end
        if min_len == N+1:
            return 0
        else:
            return min_len
