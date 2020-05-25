class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        prev = ""
        cnt = 0
        write_idx = 0
        for idx,c in enumerate(chars):
            if c != prev:
                if cnt > 0:
                    chars[write_idx] = prev
                    write_idx += 1
                    if cnt >= 2:
                        if cnt >= 100:
                            chars[write_idx] = str(int(cnt/100))
                            write_idx += 1
                        if cnt >= 10:
                            res = int((cnt-int(cnt/100)*100)/10)
                            chars[write_idx] = str(res)
                            cnt = cnt % 10
                            write_idx += 1
                        chars[write_idx] = str(cnt)
                        write_idx += 1
                prev = c
                cnt = 1
            else:
                cnt += 1
        chars[write_idx] = prev
        write_idx += 1
        if cnt >= 2:
            if cnt >= 100:
                chars[write_idx] = str(int(cnt/100))
                write_idx += 1
            if cnt >= 10:
                res = int((cnt-int(cnt/100)*100)/10)
                chars[write_idx] = str(res)
                cnt = cnt % 10
                write_idx += 1
            chars[write_idx] = str(cnt)
            write_idx += 1
        del chars[write_idx:]
        return len(chars)
