class Solution:
    def nextClosestTime(self, time: str) -> str:
        l = []
        l.append(int(time[0]))
        l.append(int(time[1]))
        l.append(int(time[3]))
        l.append(int(time[4]))
        
        if l[0] == l[1] == l[2] == l[3]:
            return time
        
        min_positive_dist = 24*60+7
        min_negative_dist = 0
        positive_candidate = ''
        negative_candidate = ''
        current_time = (l[0]*10 + l[1])*60 + l[2]*10 + l[3]
        
        for first in l:
            if first > 2: # invalid hour(HH) representation
                continue
            for second in l:
                if first*10 + second > 23: # invalid hour(HH) representation
                    continue
                for third in l:
                    if third > 5: # invalid minute(MM) representation
                        continue
                    for fourth in l:
                        current_str = str(first) + str(second) + ':' + str(third) + str(fourth)
                        if current_str == time:
                            continue
                        candidate_value = (first*10 + second)*60 + third*10 + fourth - current_time
                        if candidate_value > 0 and candidate_value < min_positive_dist:
                            min_positive_dist = candidate_value
                            positive_candidate = current_str
                        if candidate_value < 0 and candidate_value < min_negative_dist:
                            min_negative_dist = candidate_value
                            negative_candidate = current_str
        if 24*60 + min_negative_dist < min_positive_dist:
            return negative_candidate
        else:
            return positive_candidate
