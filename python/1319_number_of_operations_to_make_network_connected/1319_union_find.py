class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x):
        if self.root[x] == x: return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
      
        if self.rank[rootX] < self.rank[rootY]: self.root[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]: self.root[rootY] = rootX
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n-1: return -1
        
        uf = UnionFind(n)
        ans = n
        for a, b in connections:
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
                ans -= 1
            
        return ans - 1