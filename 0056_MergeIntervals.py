class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return [[]]
        elif len(intervals) == 1:
            return intervals
        
        intervals.sort()
        idx = 0
        while idx < len(intervals)-1:
            cur_end = intervals[idx][1]
            next_begin = intervals[idx+1][0]
            if next_begin <= cur_end:
                intervals[idx][1] = max(cur_end, intervals[idx+1][1])
                intervals.pop(idx+1)
            else:
                idx += 1
        return intervals
