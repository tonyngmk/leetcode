class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        n = len(candidates)
        
        def backtrack(combo=[], remain=target, i=0):
            if remain==0: output.append(combo[:])
            if remain < 0 : return
            
            for x in range(i, n):
                combo.append(candidates[x])
                backtrack(combo, remain-candidates[x], x)
                combo.pop()
        
        backtrack()
        return output
        