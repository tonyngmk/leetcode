from typing import List

def serialize(arr, i=0, j=0):
    """Serialize an array into a format the visualizer can understand."""
    formatted = {
        "kind": {"grid": True},
        "rows": [
            {
                "columns": [
                    {"content": str(value), "tag": str(value)} for value in arr
                ],
            }
        ],
         "markers": [
        {
            "row": 0,
            "column": i,
            "id": "i",
        },
        {
            "row": 0,
            "column": j,
            "id": "j",
        },
        ]
    }
    return formatted

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ans = len(nums)

        serialized = serialize(nums)
        
        for i, j in enumerate(nums):
            serialized = serialize(nums, i, j)
            ans ^= i ^ j
            
        return ans

# assert(Solution().missingNumber([3,0,1]) == 2)
# assert(Solution().missingNumber([0,1]) == 2)
assert(Solution().missingNumber([9,6,4,2,3,5,7,0,1]) == 8)
