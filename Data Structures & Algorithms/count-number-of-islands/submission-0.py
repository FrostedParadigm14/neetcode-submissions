class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                directions = [(1, 0), (-1,0), (0,1), (0,-1)]

                for dr, dc in directions:
                    rows, cols = row + dr, col + dc
                    if rows in range(m) and cols in range(n) and grid[rows][cols] == "1" and (rows,cols) not in visited:
                       queue.append((rows,cols)) 
                       visited.add((rows,cols))


        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands+=1
            
        return islands




'''
check on it daigonally, like parent, check childs, contunue hcek theire childs onnward
like graphs bfs
Level-by-level traversal using a queue
encounter a land cell, we use BFS to visit all connected land cells and mark them as water,

'''