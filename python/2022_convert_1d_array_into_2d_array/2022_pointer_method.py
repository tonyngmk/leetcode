class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        length = len(original)
        if (m * n) != length: return []
        
        ans = []
        i = j = 0
        
        while i < length:
            temp = []
            while i < length and j < n:
                temp.append(original[i])
                j += 1
                i += 1
            j = 0
            ans.append(temp)
            
        return ans
            