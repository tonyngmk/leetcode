class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = 0
            for R, C in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= R < m and 0 <= C < n and grid[R][C]:
                    dfs(R, C)


        for r in range(m):
            for c in range(n):
                if (r==0 or c==0 or r==m-1 or c==n-1) and grid[r][c]:
                    dfs(r, c)

        return sum([sum(grid[r]) for r in range(m)])
 