class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []

        for c in s:
            if c in m: stack.append(c)
            elif not stack: return False
            else:
                left = stack.pop()
                if m[left] != c: return False
        
        return not stack
