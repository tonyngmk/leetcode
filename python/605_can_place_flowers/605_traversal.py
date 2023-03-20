class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        i = 0
        length = len(flowerbed)
        buffer = False
        
        while i < length and n > 0:
            if buffer:
                buffer = False
                continue
            if flowerbed[i] == 1: buffer = True
            else: n -= 1
            i += 1
            
        return n == 0 
    