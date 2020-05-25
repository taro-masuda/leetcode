class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals[1:]:
            if start == interval[0]:
                return False
            elif end == interval[1]:
                return False
            elif start < interval[0] and interval[0] < end: 
                return False
            start = min(start, interval[0])
            end = max(end, interval[1])
        return True
