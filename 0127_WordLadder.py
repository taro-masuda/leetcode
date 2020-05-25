import copy

class Solution:
    def levenshtein_distance(self, w1: str, w2: str) -> int:
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
        #print("ld", count)
        return count
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #print("beginword: ", beginWord, "endWord: ", endWord)
        if beginWord == endWord:
            return 0
        elif not (endWord in wordList):
            return 0
        
        count = []
        for w in wordList:
            if self.levenshtein_distance(beginWord, w) == 1:
                current_count = 2
                
                if w == endWord:
                    #print("same word appears so append current count")
                    count.append(current_count)
                    continue
                    
                wl = copy.deepcopy(wordList)
                wl.remove(w)
                ll = self.ladderLength(w, endWord, wl)
                if ll > 0:
                    current_count += ll-1
                    count.append(current_count)
        #print("ladderlength", count)
        if len(count) == 0:
            return 0
        else:
            return min(count)
