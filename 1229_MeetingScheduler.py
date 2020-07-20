class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        i1 = 0; i2 = 0
        L1 = len(slots1); L2 = len(slots2)
        slots1.sort(); slots2.sort()
        while i1 < L1 and i2 < L2:
            slot1 = slots1[i1]; slot2 = slots2[i2]
            if (slot1[0] <= slot2[0] and (slot2[0] < slot1[1])) or \
               (slot2[0] <= slot1[0] and (slot1[0] < slot2[1])):
                begin = max(slot1[0], slot2[0]); 
                end = min(slot1[1], slot2[1])
                d = end - begin
                if d >= duration:
                    return [begin, begin+duration]
            if slot1[1] < slot2[1]:
                i1 += 1
            elif slot2[1] < slot1[1]:
                i2 += 1
            else:
                if i1 == L1-1:
                    i2 += 1
                elif i2 == L2-1:
                    i1 += 1
                elif slots1[i1+1][0] <= slots2[i2+1][0]:
                    i1 += 1
                else:
                    i2 += 1
        return []
