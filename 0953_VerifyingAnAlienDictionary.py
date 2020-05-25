class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # dictionary
        dic = {}
        for i,char in enumerate(order):
            dic[char] = i
        
        i = 0
        N = len(words)
        while i < N-1:
            w1 = words[i]
            w2 = words[i+1]
            
            j = 0
            N1 = len(w1)
            N2 = len(w2)
            while j < N1:
                if j >= N2:
                    return False
                if dic[w1[j]] < dic[w2[j]]:
                    break
                elif dic[w1[j]] > dic[w2[j]]:
                    return False
                j += 1
            i += 1
            
        return True
