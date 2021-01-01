class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        if len(s) > 0: max_len = 1
        else: max_len = 0
        cur_len = 0
        for i,c in enumerate(s):
            if c not in dic:
                dic[c] = i
                cur_len += 1
                max_len = max(max_len, cur_len)
            elif dic[c] == -1:
                dic[c] = i
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                if i-dic[c] == 1:
                    for key in dic:
                        dic[key] = -1
                    cur_len = 1
                    max_len = max(max_len, cur_len)
                else:
                    for key in dic:
                        if dic[key] < dic[c]: dic[key] = -1
                    max_len = max(max_len, cur_len)
                    cur_len = i-dic[c]
                dic[c] = i
            
        return max(max_len, cur_len)
