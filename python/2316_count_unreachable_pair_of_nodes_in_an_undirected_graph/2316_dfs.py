class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:        
        graph = {}
        
        for a, b in edges:
            if a not in graph: graph[a] = []
            graph[a].append(b)
            
            if b not in graph: graph[b] = []
            graph[b].append(a)
        
        component_list = []
        seen = set()
        
        for i in range(n):
            if i not in seen:
                stack = [i]
                seen.add(i)
                node_count = 1
                while stack:
                    node = stack.pop()
                    if node not in graph: break
                    for nei in graph[node]:
                        if nei not in seen:
                            stack.append(nei)
                            seen.add(nei)
                            node_count += 1                    
                component_list.append(node_count)
        
        if len(component_list)==1: return 0
        ans = 0
        for x in component_list:
            ans += (x * (n-x))
            n -= x
        return ans
        