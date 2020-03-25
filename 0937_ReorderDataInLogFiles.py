import numpy as np

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        letter_logs_noid = []
        digit_logs = []
        for log in logs:
            log_sp = log.split(' ')
            if log_sp[1][0].isdecimal():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort()
        for log in letter_logs:
            log_sp = log.split(' ')
            letter_logs_noid.append(' '.join(log_sp[1:]))
        sort_idx = np.argsort(letter_logs_noid)
        letter_logs_sorted = []
        for idx in sort_idx:
            letter_logs_sorted.append(letter_logs[idx])
        letter_logs_sorted.extend(digit_logs)   
        return letter_logs_sorted
