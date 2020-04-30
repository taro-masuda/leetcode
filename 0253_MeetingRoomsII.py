class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        if len(intervals[0]) == 0:
            return 1
        q_s = []
        q_e = []
        for interval in intervals:
            q_s.append(interval[0])
            q_e.append(interval[1])
        q_s.sort()
        q_e.sort()
        rooms = 0
        max_rooms = 0
        while len(q_e) > 0 or len(q_s) > 0:
            if len(q_s) == 0:
                break
            if q_e[0] < q_s[0]:
                rooms -= 1
                q_e.pop(0)
            elif q_e[0] == q_s[0]:
                rooms -= 1
                q_e.pop(0)
                rooms += 1
                q_s.pop(0)
                max_rooms = max(max_rooms, rooms)
            else:
                rooms += 1
                q_s.pop(0)
                max_rooms = max(max_rooms, rooms)
        return max_rooms
