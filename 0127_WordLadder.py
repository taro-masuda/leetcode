class Solution:   
    def __init__(self):
        self.dic = {}
    
    def makeAdjacentList(self, wordList) -> None:
        for word in wordList:
            L = len(word)
            for i in range(L):
                key = word[:i] + "*" + word[i+1:]
                if key not in self.dic:
                    self.dic[key] = [word]
                else:
                    self.dic[key].append(word)
                
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = [(beginWord,1)]
        visited = set()
        now_word = beginWord
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        self.makeAdjacentList(wordList)
        # Breadth First Search
        while len(q) > 0:
            top_word, top_dist = q[0]
            del q[0]
            L = len(top_word)
            for i in range(L):
                key = top_word[:i] + "*" + top_word[i+1:]
                if not key in self.dic:
                    continue
                for word in self.dic[key]:
                    if word == top_word:
                        continue
                    elif word == endWord:
                        return top_dist+1
                    elif word not in visited:
                        visited.add(word)
                        q.append((word,top_dist+1))
        return 0
