class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        i_push = 0; i_pop = 0
        while i_push < len(pushed) or i_pop < len(popped):
            if i_push >= len(pushed):
                if s[-1] != popped[i_pop]:
                    return False
                else:
                    s.pop(-1); i_pop += 1
                    continue
            if len(s) == 0:
                s.append(pushed[i_push]); i_push += 1
            elif s[-1] == popped[i_pop]:
                s.pop(-1); i_pop += 1
            else:
                s.append(pushed[i_push]); i_push += 1
        return True
