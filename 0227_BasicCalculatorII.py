import re

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        num_list = re.split('[+\-*/]', s)
        sign_list = re.split('\d+', s)
        sign_list.pop(-1)
        sign_list.pop(0)
        num_list = list(map(int, num_list))
        
        if len(num_list) == 0:
            return None
        
        idx = 0
        while len(sign_list) > 0:
            #print(sign_list, num_list)
            if idx >= len(sign_list):
                idx = len(sign_list) - 1
                
            if sign_list[idx] == '*':
                result = num_list[idx] * num_list[idx+1]
                sign_list.pop(idx)
                num_list.pop(idx+1)
                num_list[idx] = result
            elif sign_list[idx] == '/':
                result = int(num_list[idx] / num_list[idx+1])
                sign_list.pop(idx)
                num_list.pop(idx+1)
                num_list[idx] = result
            elif sign_list.count('*') == 0 and sign_list.count('/') == 0:
                idx = 0
                if sign_list[idx] == '+':
                    result = num_list[idx] + num_list[idx+1]
                else:
                    result = num_list[idx] - num_list[idx+1]
                sign_list.pop(idx)
                num_list.pop(idx+1)
                num_list[idx] = result
            else:
                idx += 1
            
        return num_list[0]
