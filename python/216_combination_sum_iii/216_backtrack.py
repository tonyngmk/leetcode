class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        output = []
        
        def backtrack(combo=[], remain=n, i=1):
            if len(combo) == k and remain == 0 : output.append(combo[:])
            if remain < 0 : return
            
            for x in range(i, 10):
                combo.append(x)
                backtrack(combo, remain-x, x+1)
                combo.pop()
                
        backtrack()
        return output
        