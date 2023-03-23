class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        
        def backtrack(combo=[], l=0, r=0):
            if len(combo) == (n*2) : output.append("".join(combo))
                
            if l < n:
                combo.append("(")
                backtrack(combo, l+1, r)
                combo.pop()
            
            if r < l:
                combo.append(")")
                backtrack(combo, l, r+1)
                combo.pop()
                
        backtrack()
        return output
        