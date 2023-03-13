class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        i, j = 0, len(letters)
        
        while i < j:
            mid = i + (j-i)//2
            
            if ord(letters[mid]) <= ord(target): i = mid + 1
            else: j = mid
                
        return letters[i] if i < len(letters) else letters[0]
        