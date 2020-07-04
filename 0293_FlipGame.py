class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        next_states = []
        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                next_states.append(s[:i] + '--' + s[i+2:])
        return next_states
