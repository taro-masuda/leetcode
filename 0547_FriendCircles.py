class Solution:
    def __init__(self):
        self.visited = set()
    
    def bfs(self, i, M) -> None:
        C = len(M[0])
        q = [i]
        while len(q) > 0:
            top = q[0]
            q.pop(0)
            for idx in range(C):
                if idx not in self.visited and M[top][idx] == 1:
                    q.append(idx)
                    self.visited.add(idx)
        
    def findCircleNum(self, M: List[List[int]]) -> int:
        if len(M) == 0:
            return 0
        elif len(M[0]) == 0:
            return 0
        cnt = 0
        for i,row in enumerate(M):
            for j,elem in enumerate(row):
                if i not in self.visited and M[i][j] == 1:
                    self.visited.add(i)
                    self.bfs(i,M)
                    cnt += 1
        return cnt
