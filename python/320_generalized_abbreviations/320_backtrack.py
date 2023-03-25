class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        output = []
        n = len(word)
        
        def backtrack(combo="", i=0, score=0):
            if i == n: output.append(combo + str(score) if score else combo)
            else:
                # Order of both does not matter
                backtrack(combo, i+1, score+1) # Skip current letter, increment count
                backtrack(combo + (str(score) if score else '') + word[i], i+1, 0) # Include current letter, reset count
                
        backtrack()
        return output
            