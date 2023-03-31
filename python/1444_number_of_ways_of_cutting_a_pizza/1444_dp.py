class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])

        # apples[r][c] denote number of apples on apple[r:][c:]
        apples = [[0] * (n+1) for _ in range(m+1)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                apples[r][c] = (
                    (pizza[r][c] == 'A') +
                    apples[r+1][c] +
                    apples[r][c+1] -
                    apples[r+1][c+1]
                )

        dp = [[
                [0 for _ in range(n)] for _ in range(m)
            ] for _ in range(k)] 
        dp[0] = [[int(apples[r][c] > 0) for c in range(n)] for r in range(m)]
        mod = 1e9 + 7
        for remain in range(1, k):
            for r in range(m):
                for c in range(n):
                    val = 0
                    # Check if there are still apples remaining in the next cut (horizontal + vertical)
                    for next_row in range(r+1, m):
                        if apples[r][c] - apples[next_row][c] > 0: 
                            val += dp[remain-1][next_row][c] # cut and reduce remain by 1
                    for next_col in range(c+1, n):
                        if apples[r][c] - apples[r][next_col]:
                            val += dp[remain-1][r][next_col]
                    dp[remain][r][c] = val % mod
        return int(dp[k-1][0][0])



        
