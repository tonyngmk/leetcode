class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)
        if (m*n) != length: return None
        ans = []
        
        for i in range(0, length, n):
            ans.append(original[i:i+n])
        return ans