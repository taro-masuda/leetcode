class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exclusive_times = [0]*n
        for i,log in enumerate(logs):
            if i == len(logs)-1:
                break
            li = log.split(":")
            li_plus1 = logs[i+1].split(":")
            func_id = int(li[0])
            if li[1] == li_plus1[1] == "start" or li[1] == li_plus1[1] == "end":
                duration = int(li_plus1[2]) - int(li[2])
            elif li[1] == "start" and li_plus1[1] == "end":
                if func_id != li_plus1[0]:
                    duration = int(li_plus1[2]) - int(li[2]) + 1
                else:
                    duration = int(li_plus1[2]) - int(li[2])
            else:
                duration = int(li_plus1[2]) - int(li[2]) - 1
            if li[1] == "start":
                stack.append(func_id)  
            else:
                stack.pop(-1)  
            if len(stack) > 0:
                exclusive_times[stack[-1]] += duration
        return exclusive_times
