class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        output = []
        
        def backtrack(combo=[], i=1):
            if len(combo) == k: output.append(combo[:])
                
            for x in range(i, n+1):
                combo.append(x)
                backtrack(combo, x+1)
                combo.pop()
        
        backtrack()
        return output
        