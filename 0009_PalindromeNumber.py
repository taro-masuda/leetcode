class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str_list = list(str(x))
        x_str_list_reversed = list(reversed(x_str_list))
        return x_str_list == x_str_list_reversed
