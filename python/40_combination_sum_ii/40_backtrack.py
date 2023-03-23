class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        n = len(candidates)
        
        def backtrack(combo=[], remain=target, i=0):
            if remain == 0 : output.append(combo[:])
            if remain < 0 : return
            
            for x in range(i, n):
                if x > i and candidates[x] == candidates[x-1]: continue
                    
                combo.append(candidates[x])
                backtrack(combo, remain-candidates[x], x+1)
                combo.pop()
                
        backtrack()
        return output
        