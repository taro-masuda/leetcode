import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        else:
            s = re.sub(re.compile("[!-/:-@[-`{-~]"), '', s).replace(" ", "").replace(",","").replace(".","").lower()
            #print(s)
            for i in range(int(len(s)/2)):
                #print(s[i], s[-i])
                if s[i] == s[-(i+1)]:
                    pass
                else:
                    return False
            
            return True
