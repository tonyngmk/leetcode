# x = 4; ans = 2
x = 8; ans = 2


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=2
        j=x/2
        m=0
        while i <= j:
            m = i + (j-i)//2
            if m**2 == x:
                return m
            elif m**2 < x:
                i = m + 1
            else:
                j = m - 1
        
        return int(m)

solution = Solution()
print(solution.mySqrt(x))
print(x, ans)