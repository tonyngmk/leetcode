class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits: return []
        
        M = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        output = []
        n = len(digits)
        
        def backtrack(combo=[], i=0):
            if len(combo)==n: output.append("".join(combo))
                
            for x in range(i, n):
                for c in M[digits[x]]:
                    combo.append(c)
                    backtrack(combo, x+1)
                    combo.pop()
                
        backtrack()
        return output
                