arr = [1,0,2,3,0,4,5,0]
ans = [1,0,0,2,3,0,0,4]

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        l = len(arr) - 1
        counter = 0
        for i in range(l+1):
            if i > l - counter:
                break

            if arr[i] == 0:
                if i == l - counter:
                    arr[l] = 0
                    l-=1
                    break
                counter += 1

        for i in range(l-counter, -1, -1):
            if arr[i] == 0:
                arr[i+counter] = 0
                counter -= 1
                arr[i+counter] = 0
            else:
                arr[i+counter] = arr[i]

solution = Solution()
print(solution.duplicateZeros(arr))
print(ans)