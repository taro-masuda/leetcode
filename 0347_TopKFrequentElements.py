class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        cnts = []
        for elem in d:
            cnts.append(d[elem])
        cnts.sort()
        out = []
        for elem in d:
            if d[elem] >= cnts[-k]:
                out.append(elem)
                
        return out
