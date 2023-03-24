class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        # Creating 2 graphs
        
        graph = {}
        anti_graph = {}
        
        for a, b in connections:
            if a not in graph: graph[a] = []
            graph[a].append(b)
            
        for a, b in connections:
            if b not in anti_graph: anti_graph[b] = []
            anti_graph[b].append(a)
            
            
        q = collections.deque([0])
        visit = set([0])
        ans = 0
        
        while q:
            node = q.popleft()
            if node in graph:
                for nei in graph[node]:
                    if nei not in visit:
                        ans += 1
                        q.append(nei)
                        visit.add(nei)
                
            if node in anti_graph:
                for nei in anti_graph[node]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)

        return ans
                
        