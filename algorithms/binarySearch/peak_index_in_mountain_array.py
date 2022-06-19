# arr = [0,1,0]; ans = 1
# arr = [0,2,1,0]; ans = 1
arr = [0,10,5,2]; ans = 1


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(A)
        i, j = 1, n-2
        
        while i <= j:
            mid = i + (j-i)//2
            if A[mid-1] < A[mid] > A[mid+1]:
                return mid
            elif A[mid-1] < A[mid]:
                i = mid + 1
            else:
                j = mid - 1 
        return mid


solution = Solution()
print("Question:", arr, ans)
print("Answer", solution.peakIndexInMountainArray(arr))