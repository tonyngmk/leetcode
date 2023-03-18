class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 2: return True
        
        i, j = 0, num/2
        
        while i <= j:
            mid = i + (j-i)//2
            x = mid ** 2
            if x==num: return True
            elif x < num: i = mid + 1
            else : j = mid - 1
                
        return False
    