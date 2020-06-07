class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        times = 1
        N_a = len(A); N_b = len(B)
        if N_a == N_b == 0:
            return 1
        hb = B
        A_rep = copy.deepcopy(A)
        while len(A_rep) < N_b + N_a:
            A_rep += A
        for i in range(N_a):
            ha = A_rep[i:i+N_b]
            if ha == hb:
                return ceil( (i+N_b)/N_a )
        return -1
