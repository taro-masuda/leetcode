class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        w_dic_list = []
        w_value_list = []
        for word in words:
            w_dic = {}
            for char in word:
                if not char in w_dic:
                    w_dic[char] = 1
                else:
                    w_dic[char] += 1
            w_dic_list.append(w_dic)
        for w_dic in w_dic_list:
            for i in range(26):
                if chr(ord('a') + i) in w_dic:
                    w_value_list.append(w_dic[chr(ord('a') + i)])
                    break
        w_value_list.sort(reverse=True)
        
        out = []
        for q in queries:
            q_dic = {}
            for char in q:
                if not char in q_dic:
                    q_dic[char] = 1
                else:
                    q_dic[char] += 1
            q_small_freq = 0
            for i in range(26):
                    if chr(ord('a') + i) in q_dic:
                        q_small_freq = q_dic[chr(ord('a') + i)]
                        break
            for i, w_value in enumerate(w_value_list):
                if q_small_freq >= w_value:
                    out.append(i)
                    break
                if i == len(w_value_list)-1:
                    out.append(i+1)
        
        return out
