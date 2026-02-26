from typing import List

def find_lexicographically_largest_string(word: str, numFriends: int) -> str:
    """
    Find the lexicographically largest string from the box after all rounds are finished.
    
    In this game, Alice splits the word into numFriends non-empty strings in each round,
    such that no previous round has had the exact same split. All split words are put into a box.
    
    Args:
        word: A string consisting of lowercase English letters
        numFriends: Number of friends (and number of splits per round)
        
    Returns:
        The lexicographically largest string from the box
    
    Example:
        Input: word = "dbca", numFriends = 2
        Output: "dbc"
        
        Input: word = "gggg", numFriends = 4
        Output: "g"
    """
    # Generate all possible ways to split the word into numFriends parts
    all_splits = []
    
    def generate_splits(start_idx: int, parts_remaining: int, current_splits: List[str]):
        if parts_remaining == 0:
            if start_idx == len(word):
                all_splits.append(current_splits.copy())
            return
        
        for i in range(start_idx + 1, len(word) + 1):
            # Each part must be non-empty
            if i > start_idx:
                current_splits.append(word[start_idx:i])
                generate_splits(i, parts_remaining - 1, current_splits)
                current_splits.pop()
    
    generate_splits(0, numFriends, [])
    
    # Collect all strings from the box
    box = []
    for split in all_splits:
        box.extend(split)
    
    # Return the lexicographically largest string
    return max(box) if box else ""


def test_find_lexicographically_largest_string():
    # Test case 1
    word1 = "dbca"
    numFriends1 = 2
    expected1 = "dbc"
    result1 = find_lexicographically_largest_string(word1, numFriends1)
    print(f"Test case 1: {'Passed' if result1 == expected1 else 'Failed'} - Expected: {expected1}, Got: {result1}")
    
    # Test case 2
    word2 = "gggg"
    numFriends2 = 4
    expected2 = "g"
    result2 = find_lexicographically_largest_string(word2, numFriends2)
    print(f"Test case 2: {'Passed' if result2 == expected2 else 'Failed'} - Expected: {expected2}, Got: {result2}")


if __name__ == "__main__":
    test_find_lexicographically_largest_string()