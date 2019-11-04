class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        x_str_list = list(x_str)
        if x_str_list[0] == '-':
            x_str_reversed = '-'+''.join(list(reversed(x_str[1:])))
            if int(x_str_reversed) <= -2**31:
                return 0
        else:
            x_str_reversed = ''.join(list(reversed(x_str)))
            if int(x_str_reversed) > 2**31:
                return 0
        return int(x_str_reversed)
