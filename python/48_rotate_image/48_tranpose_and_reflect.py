class Solution:
    def transpose(self, matrix):
        for i in range(self.n):
            for j in range(i+1, self.n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def reflect(self, matrix):
        for i in range(self.n):
            for j in range(self.n//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.n = len(matrix)
        self.transpose(matrix)
        self.reflect(matrix)