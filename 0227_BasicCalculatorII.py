class Solution:
    def calculate(self, s: str) -> int:
        signs = []; nums = []
        digitup = 0
        for i, char in enumerate(s):
            if char == " ":
                continue
            elif char == "+" or char == "-" or char == "*" or char == "/":
                signs.append(char)
                digitup = 0
            elif digitup == 0:
                nums.append(digitup*10 + int(char))
                digitup = int(digitup*10 + int(char))
            else:
                nums[-1] *= 10
                nums[-1] += int(char)
                digitup = nums[-1]
        idx = 0
        while idx < len(signs):
            if signs[idx] == "+" or signs[idx] == "-":
                idx += 1
                continue
            elif signs[idx] == "*":
                nums[idx] *= nums[idx+1]
                nums.pop(idx+1); signs.pop(idx)
            else:
                nums[idx] = int(nums[idx] / nums[idx+1])
                nums.pop(idx+1); signs.pop(idx)
            
        while len(signs) > 0:
            if signs[0] == "+":
                nums[0] += nums[1]
            else:
                nums[0] -= nums[1]
            nums.pop(1); signs.pop(0)
        return nums[0]
