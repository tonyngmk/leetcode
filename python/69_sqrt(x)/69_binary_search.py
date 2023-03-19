class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2: return x
        
        i, j = 2, x//2
        
        while i <= j:
            mid = i + (j-i)//2
            check = mid**2
            if check == x: return mid
            elif check < x: i = mid + 1
            else: j = mid - 1
                
        return j