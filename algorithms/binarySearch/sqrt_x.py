# x = 4; ans = 2
x = 8; ans = 2


from math import e, log

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # # Approach 1: pocket calculator
        # if x < 2: return x
        # root = int(e**(0.5 * log(x)))
        # root_plus = root + 1
        # return root if root_plus**2 > x else root_plus
    
        # Approach 2 : binary search
        
        i=2
        j=x/2
        m=x
        if x < 2: return x
        while i <= j:
            m = i + (j-i)//2
            if m**2 == x:
                return m
            elif m**2 < x:
                i = m + 1
            else:
                j = m - 1
        
        return j


solution = Solution()
print(solution.mySqrt(x))
print(x, ans)