class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_added = digits[:]
        updigit = 1
        for i in reversed(range(len(digits))):
            digits_added[i] = (digits[i] + updigit) % 10
            updigit = int((digits[i] + updigit) / 10) # 10になったときだけ1
        if updigit == 1: # 最後の最後で繰り上がったら最初に1を追加
            digits_added.insert(0, 1)
        return digits_added
