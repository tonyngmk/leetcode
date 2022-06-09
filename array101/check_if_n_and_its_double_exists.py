arr = [10,2,5,3]
ans = True

# Constraints:

# 2 <= arr.length <= 500
# -10^3 <= arr[i] <= 10^3

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        myMap = {}

        for i in arr:
            if (2*i in myMap) or (i%2==0 and i//2 in myMap):
                return True
            else:
                myMap[i] = None

        return False
        
        # def iterative_binary_search(arr, x):            
        #     i = 0
        #     j = len(arr) - 1
            
        #     while i <= j:

        #         mid = i + (j - i) // 2
        #         if arr[mid] == x:
        #             return True

        #         elif arr[mid] < x:
        #             i = mid + 1

        #         else:
        #             j = mid - 1

        #     return False


        # def recursive_binary_search(arr, i, j, x):
        #     # dynamic parameter
        #     mid = i + (j-i)//2

        #     # base + recursive case
        #     if i <= j:
        #         # base case
        #         if x == arr[mid]:
        #             return mid
        #         # recursive case (pt. 1)
        #         elif x < arr[mid]:
        #             return recursive_binary_search(arr, i, mid-1, x)
        #         # recursive case (pt. 2)
        #         elif x > arr[mid]:
        #             return recursive_binary_search(arr, mid+1, j, x)

        # return recursive_binary_search(sorted(arr), 0, len(arr)-1, 10)
        # return iterative_binary_search(sorted(arr), 3)
        
print("Input", sorted(arr), ans)
solution = Solution()
print(solution.checkIfExist(arr))
