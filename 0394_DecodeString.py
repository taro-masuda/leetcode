class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        muls = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == '[':
                n_bla = 1
                sub = ''
                i += 1
                while n_bla > 0:
                    if s[i] == ']':
                        n_bla -= 1
                        if n_bla == 0:
                            i += 1
                            break
                    elif s[i] == '[':
                        n_bla += 1
                    sub += s[i]
                    i += 1
                decode_sub = self.decodeString(sub)
                for _ in range(muls[-1]):
                    ans += decode_sub
                muls.pop(-1)
            else:
                if c >= '0' and c <= '9':
                    val = int(c)
                    i += 1
                    while s[i] >= '0' and s[i] <= '9':
                        val = val * 10 + int(s[i])
                        i += 1
                    muls.append(val)
                else:
                    ans += c
                    i += 1
        return ans
