class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        s = s.lower()
        
        output = []
        n = len(s)
        
        def backtrack(combo=[], i=0):
            if i == n: output.append("".join(combo))
            if i >= n: return
            
            if s[i].isdigit():
                combo.append(s[i])
                backtrack(combo, i+1)
                combo.pop()
                
            else:
                for x in [s[i], s[i].upper()]:
                    combo.append(x)
                    backtrack(combo, i+1)
                    combo.pop()
            
        backtrack()
        return output
        
        