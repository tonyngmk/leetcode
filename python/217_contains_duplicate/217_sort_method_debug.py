from typing import List

def serialize(arr, i=0):
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
    ]
    }
    return formatted

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        serialized = serialize(nums, 0)
        nums.sort()
        serialized = serialize(nums, 0)
        
        for i in range(1, len(nums)):
            serialized = serialize(nums, i)
            if nums[i] == nums[i-1]: return True
        return False


# assert(Solution().containsDuplicate([1,2,3,1])==True)
# assert(Solution().containsDuplicate([1,2,3])==False)
assert(Solution().containsDuplicate([6,5,4,3,2,1,7,7])==True)