A = [1,2,4,4]
ans = [3]

class Solution(object):
    def findDisappearedNumbers(self, A):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach 1: Hash set, Time: O(n), Space: O(n)
        return set(i for i in range(1, len(A)+1)) ^ set(A)
        
solution = Solution()
print(solution.findDisappearedNumbers(A))
print(A, ans)