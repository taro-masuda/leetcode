class Solution:
    def __init__(self):
        self.dic = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_copy = s[:]
        s_history = []
        if s in self.dic:
            return self.dic[s]
        if s == '' or s.replace(' ', '') == '':
            self.dic[s] = True
            return True
        for word in wordDict:
            if word in s_copy:
                s_history.append(s_copy)
                s_copy = s_copy.replace(word, ' ')
                if self.wordBreak(s_copy, wordDict):
                    self.dic[s] = True
                    return True
                else:
                    s_copy = s_history[-1];
                    s_history.pop();
        self.dic[s] = False
        return False
