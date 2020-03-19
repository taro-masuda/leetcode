class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        elif len(intervals[0]) == 0:
            return [[]]
        st = intervals[0][0]
        end = intervals[0][1]
        times = {}
        for l in intervals:
            if st > l[0]:
                st = l[0]
            if end < l[1]:
                end = l[1]
            for i in range(l[0],l[1]):
                times[i] = 1 # 1=connected to next number
            if l[0] == l[1]:
                if l[0] not in times:
                    times[l[0]] = 0
            if l[1] not in times:
                times[l[1]] = 0 # 0=disconnected to next number
        out = []
        l = []
        for i in range(st,end+1):
            if i in times:
                if times[i] == 1 and len(l) == 0:
                    l.append(i)
                elif times[i] == 0 and len(l) == 1:
                    l.append(i)
                    out.append(l)
                    l = []
                elif times[i] == 0 and len(l) == 0:
                    l.append(i)
                    l.append(i)
                    out.append(l)
                    l = []
            elif len(l) > 0:
                l.append(i-1)
                out.append(l)
                l = []
        if len(l) > 0:
            l.append(end)
            out.append(l)
        return out
