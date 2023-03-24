class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        # Creating only 1 graph, turn DAG to undirected
        
        graph = {}
        
        for a, b in connections:
            if a not in graph: graph[a] = []
            graph[a].append((b, True))
            
            if b not in graph: graph[b] = []
            graph[b].append((a, False))
            
        q = collections.deque([0])
        visit = set([0])
        ans = 0
        
        while q:
            node = q.popleft()
            if node in graph:
                for nei, is_connected in graph[node]:
                    if nei not in visit:
                        ans += is_connected
                        q.append(nei)
                        visit.add(nei)

        return ans
                
        