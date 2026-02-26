from typing import List
class Solution:
    def __init__(self):
        self.prices = [7,1,5,3,6,4]
        print(self.maxProfit(self.prices))

    def maxProfit(self, prices: List[int]) -> int:
        x = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > x: 
                profit += prices[i] - x
            x = prices[i]
        return profit

sol = Solution()