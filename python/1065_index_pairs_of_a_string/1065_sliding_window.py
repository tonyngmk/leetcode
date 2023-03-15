class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        
        ans = []
        n = len(text)
        for i in range(n):
            for word in words:
                n_word = len(word)
                if i <= (n - n_word) and word[0] == text[i]:
                    a, b = i, 0
                    match = True
                    
                    while a < n and b < n_word:
                        if text[a] != word[b]:
                            match = False
                            break
                        a += 1
                        b += 1
                    
                    if match: ans.append((i, i+n_word-1))
                  
        ans.sort(key = lambda x: (x[0], x[1]))
        return ans
                    
