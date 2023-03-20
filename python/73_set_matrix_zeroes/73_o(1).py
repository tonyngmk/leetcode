class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        is_row = is_col = False
        
        if matrix[0][0] == 0:
            is_row = is_col = True
            
        else:
            for r in range(m):
                if matrix[r][0]==0:
                    is_row=True
                    break
                    
            for c in range(n):
                if matrix[0][c]==0:
                    is_col=True
                    break
                
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c]==0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                    
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c]==0 or matrix[r][0]==0: matrix[r][c] = 0
                    
        
        if is_row:
            for r in range(m):
                matrix[r][0] = 0
                
        if is_col:
            for c in range(n):
                matrix[0][c] = 0
                
        return matrix
        