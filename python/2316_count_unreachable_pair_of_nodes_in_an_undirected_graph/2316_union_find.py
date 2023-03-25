class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x):
        if self.root[x] == x: return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        
        if self.rank[rootX] < self.rank[rootY]: self.root[rootX] = rootY 
        elif self.rank[rootY] < self.rank[rootX]: self.root[rootY] = rootX
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:        
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        
        c = {}
        for i in range(n):
            root = uf.find(i)
            if root not in c: c[root] = 0
            c[root] += 1
                
        ans = 0
        for v in c.values():
            ans += v * (n-v)
            n -= v
        return ans