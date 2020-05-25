class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)):
            charSet = set()
            currLen = 0
            j = i
            isBreak = False
            while j < len(s):
                if s[j] not in charSet:
                    charSet.add(s[j])
                    currLen += 1
                    j += 1
                else:
                    maxLen = max(currLen, maxLen)
                    isBreak = True
                    break
            if not isBreak:
                maxLen = max(maxLen, j-i)
        return maxLen
