class Solution:
    def addDigits(self, num: int) -> int:

        if not num: return 0
        x = num % 9
        return 9 if not x else x
