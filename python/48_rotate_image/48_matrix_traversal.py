class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        t = l = 0
        b, r = len(matrix)-1, len(matrix[0])-1
        
        while t<b and l<r:
            for i in range(r-l):
                top_left = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = top_left
                
            t += 1
            l += 1
            r -= 1
            b -= 1
            
        return matrix
    