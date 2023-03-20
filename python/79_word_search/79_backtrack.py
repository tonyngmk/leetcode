class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        seen = set()
        
        def backtrack(r, c, i):
            if i == len(word): return True
            if i > len(word): return
            
            if not (
                0 <= r < m and 
                0 <= c < n and 
                board[r][c] == word[i] and
                (r, c) not in seen
            ): return False
            
            seen.add((r, c))
            ans = (
                backtrack(r+1, c, i+1) or
                backtrack(r-1, c, i+1) or
                backtrack(r, c+1, i+1) or
                backtrack(r, c-1, i+1)
            )
            seen.remove((r, c))
            return ans
            
            
        for r in range(m):
            for c in range(n):
                if word[0] == board[r][c] and backtrack(r, c, 0): return True
                
        return False