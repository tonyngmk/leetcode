class TrieNode:
    def __init__(self):
        self.flag = False
        self.next = dict()
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        root = self.root
        for c in word:
            if c not in root.next: root.next[c] = TrieNode()
            root = root.next[c]
        root.flag = True # mark the end node as True
            
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for word in words: trie.insert(word)
        
        ans = []
        
        for i in range(len(text)):
            root = trie.root
            for j in range(i, len(text)):
                if text[j] not in root.next: break
                
                root = root.next[text[j]]
                if root.flag: ans.append([i, j])
                    
        return ans
        