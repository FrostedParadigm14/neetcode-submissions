class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perm = 0
        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if r - 1 < 0 or grid[r-1][c] == 0:
                        perm+=1
                    if r + 1 >= m or grid[r+1][c] == 0:
                        perm+=1
                    if c - 1 < 0 or grid[r][c-1] == 0:
                        perm+=1
                    if c + 1 >= n or grid[r][c+1] == 0:
                        perm+=1
        
        return perm

        
        