class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        combo = []
        n = len(nums)
        
        counter = {}
        for num in nums:
            if num not in counter: counter[num] = 0
            counter[num] += 1
            
        def backtrack():
            if len(combo) == n: output.append(combo[:])
            
            for num in counter:
                if counter[num] > 0:
                    combo.append(num)
                    counter[num] -= 1
                    
                    backtrack()
                    
                    combo.pop()
                    counter[num] += 1
                    
        backtrack()
        return output
            