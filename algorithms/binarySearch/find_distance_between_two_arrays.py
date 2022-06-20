class Solution(object):
    def findTheDistanceValue(self, A1, A2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        A2 = sorted(A2)
        n = len(A2)
        i, j = 0, n-1
        count = 0
        for a in A1:
            while i<=j:
                mid = i + (j-i)/2
                if abs(a-A2[mid]) <= d:
                    count-=1
                    break
                # elif a <= A2[mid]:
                #     j = mid - 1
                else:
                    j = mid - 1
                    # i = mid + 1

            i, j = 0, n-1 # reset
            count+=1
        return count

solution = Solution()
print("Question: ", arr1, arr2, d)
print("Answer: ", solution.findTheDistanceValue(arr1, arr2, d))