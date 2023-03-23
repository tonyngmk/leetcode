class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n-1: return -1
        
        graph = {}
        for a, b in connections:
            if a not in graph: graph[a] = []
            graph[a].append(b)
            
            if b not in graph: graph[b] = []
            graph[b].append(a)
        
        connected = 0
        seen = set()
        
        for i in range(n):
            if i not in seen:

                connected += 1

                # DFS
                if i not in graph: continue
                seen.add(i)
                stack = [i]
                
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                            
                
        return connected-1
            