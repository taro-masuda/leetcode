class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        ans = []
        countup = 0
        for i in range(length):
            if i >= len(a):
                ai = '0'
            else:
                ai = a[-i-1]
            if i >= len(b):
                bi = '0'
            else:
                bi = b[-i-1]
            if ai == bi:
                if countup == 0:
                    ans.append('0')
                else:
                    ans.append('1')
                if ai == '1':
                    countup = 1
                else:
                    countup = 0
            else: 
                if countup == 0:
                    ans.append('1')
                    countup = 0
                else:
                    ans.append('0')
                    countup = 1
        if countup == 1:
            ans.append('1')
        ans.reverse()
        return ''.join(ans)
