class Solution:
    def __init__(self):
        self.visited = set()
        self.R = None
        self.C = None
    
    def BFS(self, grid: List[List[int]], q) -> int:
        area = 0
        while len(q) > 0:
            r_top, c_top = q[0]
            q.pop(0)
            if (r_top, c_top) not in self.visited:
                self.visited.add((r_top, c_top))
                area += 1
            else:
                continue
            # top
            if r_top > 0:
                if (r_top-1, c_top) not in self.visited and grid[r_top-1][c_top] == 1:
                    q.append((r_top-1, c_top))
            # bottom
            if r_top < self.R-1:
                if (r_top+1, c_top) not in self.visited and grid[r_top+1][c_top] == 1:
                    q.append((r_top+1, c_top))
            # left
            if c_top > 0:
                if (r_top, c_top-1) not in self.visited and grid[r_top][c_top-1] == 1:
                    q.append((r_top, c_top-1))
            # right
            if c_top < self.C-1:
                if (r_top, c_top+1) not in self.visited and grid[r_top][c_top+1] == 1:
                    q.append((r_top, c_top+1))
        return area
            
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.R = len(grid)
        if self.R == 0:
            return 0
        self.C = len(grid[0])
        max_area = 0
        for r in range(self.R):
            for c in range(self.C):
                if grid[r][c] == 1 and (r,c) not in self.visited:
                    max_area = max(max_area, 1)
                    q = []
                    q.append((r,c))
                    max_area = max(max_area, self.BFS(grid, q))
        return max_area
