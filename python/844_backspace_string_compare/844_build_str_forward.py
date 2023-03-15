class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def build_str(s):
            ans = []
            
            for x in s:
                if x != '#': ans.append(x)
                elif ans: ans.pop()
            return "".join(ans)
        
        return build_str(s) == build_str(t)
    