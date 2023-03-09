class Solution:

    def serialize(self, arr, i=0, j=0):
        """Serialize an array into a format the visualizer can understand."""
        formatted = {
            "kind": {"grid": True},
            "rows": [
                {
                    "columns": [
                        {"content": str(value), "tag": str(value)} for value in arr
                    ],
                }
            ],
            "markers": [
                {
                    "row": 0,
                    "column": i,
                    "id": "i",
                    "id": "i"
                },
                {
                    "row": 0,
                    "column": j,
                    "id": "j",
                    "id": "j"
                }
            ]
        }
        return formatted

    def isPalindrome(self, s: str) -> bool:
        
        i, j = 0, len(s)-1
        serialized = self.serialize(s, i, j)

        while i <= j:
            if not s[i].isalnum() and not s[j].isalnum():
                i += 1
                j -= 1
                serialized = self.serialize(s, i, j)
                continue
            if not s[i].isalnum():
                i += 1
                serialized = self.serialize(s, i, j)
                continue
            if not s[j].isalnum():
                j -= 1
                serialized = self.serialize(s, i, j)
                continue
            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1
            serialized = self.serialize(s, i, j)
            
        return True
        
test_in = "A man, a plan, a canal: Panama"
test_out = True
print(Solution().isPalindrome(test_in)==test_out)
