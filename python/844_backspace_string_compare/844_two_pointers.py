class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1 # Pointer s, Pointer t
        a = b = 0 # Skip s, Skip t
        
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    a += 1
                    i -= 1
                elif a:
                    a -= 1
                    i -= 1
                else: break
                    
                    
            while j >= 0:
                if t[j] == "#":
                    b += 1
                    j -= 1
                elif b:
                    b -= 1
                    j -= 1
                else: break
            
            if i >= 0 and j >= 0 and s[i] != t[j]: return False # string does not match after processing
            if (i >= 0) != (j >= 0): return False # 1 string has finished while the other has not
            
            i -= 1
            j -= 1
            
        return True
        