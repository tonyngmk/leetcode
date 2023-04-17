class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        M = max(candies)
        return [True if (c + extraCandies) >= M else False for c in candies]
