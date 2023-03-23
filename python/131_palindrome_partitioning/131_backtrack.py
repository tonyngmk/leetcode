class Solution:
    def is_pali(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True
        
    def partition(self, s: str) -> List[List[str]]:
        output = []
        n = len(s)
        def backtrack(combo=[], i=0):
            if i == n : output.append(combo[:])
                
            for x in range(i, n):
                if self.is_pali(s[i: x+1]):
                    combo.append(s[i:x+1])
                    backtrack(combo, x+1)
                    combo.pop()
        backtrack()
        return output