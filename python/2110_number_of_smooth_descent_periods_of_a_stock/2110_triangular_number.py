class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        ans = temp_ans = 1
        prev = prices[0]
        
        for price in prices[1:]:
            if (prev-price)==1: temp_ans += 1
            else: temp_ans = 1
            prev = price
                
            ans += temp_ans
                
        return ans
    