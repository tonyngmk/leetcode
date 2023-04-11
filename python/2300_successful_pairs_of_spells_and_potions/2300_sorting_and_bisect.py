class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        max_potion = potions[-1]
        ans = []
        m = len(potions)

        for spell in spells:
            min_potion_required = math.ceil(success / spell)
            if min_potion_required > max_potion: ans.append(0)

            else:
                i, j = 0, len(potions)-1
                while i < j:
                    mid = i + (j-i)//2
                    if potions[mid] < min_potion_required: i = mid + 1
                    else: j = mid
                
                ans.append(m-i)

        return ans
