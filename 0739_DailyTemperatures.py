class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        warmer_day = [0]*len(T)
        recent_day = [2**31-1]*101
        MAXLEN = 30000
        for i in range(len(T)-1, -1, -1):
            minday = 2**31-1
            for warmer_temp in range(T[i]+1, 101):
                if recent_day[warmer_temp] <= MAXLEN:
                    minday = min(minday, recent_day[warmer_temp]-i)
            if minday <= MAXLEN:
                warmer_day[i] = minday
            recent_day[T[i]] = i
        return warmer_day
