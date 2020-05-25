class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        maxnum = 0
        for word in words:
            if not word in dic:
                dic[word] = 1
                maxnum = max(maxnum, dic[word])
            else:
                dic[word] += 1
                maxnum = max(maxnum, dic[word])
        out = []
        for freq in range(maxnum, 0, -1):
            l = []
            for (key,v) in dic.items():
                if freq == v:
                    l.append(key)
            l.sort()
            out.extend(l)
            if len(out) >= k:
                out = out[:k]
                break
                
        return out
