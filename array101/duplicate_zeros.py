arr = [1,0,2,3,0,4,5,0]
ans = [1,0,0,2,3,0,0,4,5,0,0]

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        copy_arr = [i for i in arr]

        # Write from front
        i2 = 0 # pointer for writing
        # i is the pointer for value
        for i in range(l):
            if i2 > l-1:
                break
            if copy_arr[i] == 0:
                arr[i2] = 0
                i2 += 1
                if i2 <= l-1:
                    arr[i2] = 0
                else:
                    break
                i2 += 1
            else:
                arr[i2] = copy_arr[i]
                i2 +=1
        return arr
solution = Solution()
print(solution.duplicateZeros(arr))