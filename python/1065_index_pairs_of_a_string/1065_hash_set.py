class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        
        words = set(words)
        ans = []
        n = len(text)
        for i in range(n):
            for word in words:
                n_word = len(word)
                if (i + n_word - 1) < n and word[0] == text[i] and text[i:i+n_word] == word:
                    ans.append([i, i+n_word-1])
        
        ans.sort(key = lambda x: (x[0], x[1]))
        return ans