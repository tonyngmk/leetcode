# num = 16; ans = True
num = 14; ans = False

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 2: return True
        
        i = 2
        j = num/2
        while i <= j:
            m = i + (j-i)/2
            print(i, m, j)
            if m**2 == num:
                return True
            elif m**2 < num:
                i = m + 1
            else:
                j = m - 1
        return False


solution = Solution()
print("Question: ", num, ans)
print("Answer: ", solution.isPerfectSquare(num))