class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def build_str(s):
            ans = ""
            skip = 0
            
            for x in s[::-1]:
                if x == '#':
                    skip += 1
                    continue
                
                if skip:
                    skip -= 1
                    continue
                    
                ans += x

            return ans[::-1]
        
        return build_str(s) == build_str(t)
    