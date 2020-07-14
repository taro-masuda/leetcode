class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        l = [[] for i in range(1001)]
        for record in items:
            id_st = record[0]
            score = record[1]
            l[id_st].append(score)
        ave = [[] for i in range(1001)]
        for i in range(len(l)):
            if len(l[i]) == 0:
                ave[i] = [0, i]
            else:
                l[i].sort(reverse=True)
                maxidx = min(len(l[i]), 5)
                ave[i] = [int(sum(l[i][:maxidx]) / maxidx), i]
        ans = []
        for i in range(len(ave)):
            if ave[i][0] == 0:
                continue
            ans.append([ave[i][1], ave[i][0]])
        return ans
