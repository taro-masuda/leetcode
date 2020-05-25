class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        for i,tp in enumerate(timePoints):
            hour = int(tp.split(":")[0])
            minute = int(tp.split(":")[1])
            minutes = hour*60 + minute
            timePoints[i] = minutes
        
        min_diff = 24*60
        for i,tp1 in enumerate(timePoints):
            for j,tp2 in enumerate(timePoints):
                if i==j:
                    continue
                diff1 = abs(tp1-tp2)
                if tp1 < tp2:
                    diff2 = tp1+24*60-tp2
                else:
                    diff2 = tp2+24*60-tp1
                min_diff = min(min_diff, diff1, diff2)
                
        return min_diff
