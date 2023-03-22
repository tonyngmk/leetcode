class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = collections.defaultdict(dict)
        for a, b, w in roads:
            graph[a][b] = graph[b][a] = w
            
        ans = float('inf')
        seen = set()
        q = collections.deque([1])
        
        while q:
            node = q.popleft()
            for nei, w in graph[node].items():
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)
                ans = min(ans, w)
        return ans
            