nums = [4,3,2,7,8,2,3,1]
ans = [5,6]

class Solution(object):
    def findDisappearedNumbers(self, A):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(A) # T: O(1), S: O(1)
        S1 = {i for i in range(1, n+1)} # T: O(n), S: O(n)
        S2 = set(A) # T: O(n), S: O(n)
        return list(S1 ^ S2) # Likely O(2n) ?
        
solution = Solution()
print("Question: ", nums, ans)
print("Answer:", solution.findDisappearedNumbers(nums))