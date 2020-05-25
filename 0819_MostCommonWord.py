class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(",", " ").replace(".", " ")
        paragraph = ''.join([i for i in paragraph if i.isalpha() or i == ' '])
        list_para = paragraph.lower().split(" ")
        dic = {}
        banned_set = set(banned)
        largest = 0
        for word in list_para:
            if word == "" or word == " ":
                continue
            if word in banned_set:
                continue
            if word not in dic:
                dic[word] = 1
                largest = max(largest, 1)
            else:
                dic[word] += 1
                largest = max(largest, dic[word])
        
        for key,val in dic.items():
            if val == largest:
                return key
