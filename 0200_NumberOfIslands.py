class Solution:
    def __init__(self):
        self.visited = set()
        
    def bfs(self, grid, i, j):
        R = self.R; C = self.C
        q = [(i,j)]
        while len(q) > 0:
            r, c = q.pop(0)
            if r < R-1:
                if grid[r+1][c] == "1" and (r+1,c) not in self.visited:
                    q.append((r+1,c))
                    self.visited.add((r+1,c))
            if c < C-1:
                if grid[r][c+1] == "1" and (r,c+1) not in self.visited:
                    q.append((r,c+1))
                    self.visited.add((r,c+1))
            if r > 0:
                if grid[r-1][c] == "1" and (r-1,c) not in self.visited:
                    q.append((r-1,c))
                    self.visited.add((r-1,c))
            if c > 0:
                if grid[r][c-1] == "1" and (r,c-1) not in self.visited:
                    q.append((r,c-1))
                    self.visited.add((r,c-1))
            
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.R = len(grid)
        if self.R == 0:
            return 0
        self.C = len(grid[0])
        if self.C == 0:
            return 0
        num = 0
        for i,row in enumerate(grid):
            for j,elem in enumerate(row):
                if elem == "1" and (i,j) not in self.visited:
                    self.visited.add((i,j))
                    num += 1
                    self.bfs(grid,i,j)
        return num
