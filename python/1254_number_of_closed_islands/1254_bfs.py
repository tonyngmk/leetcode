class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        seen = set()
        ans = 0

        def bfs(r, c):
            q = collections.deque([(r, c)])
            isClosed = True
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                        R, C = r+x, c+y
                        if (R < 0) or (R >= m) or (C < 0) or (C >= n): isClosed = False
                        if 0 <= R < m and 0 <= C < n and grid[R][C] == 0 and (R, C) not in seen:
                            seen.add((R,C))
                            q.append((R,C))
            return isClosed

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and (r, c) not in seen and bfs(r, c): ans += 1
        return ans
