class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans = -1
        visit = set()
    
        for i in range(len(edges)):
            if edges[i] == -1 or i in visit: continue
            
            visit.add(i)
            stack = [i]
            d = {i:1}
            while stack:
                node = stack.pop()
                nei = edges[node]
                if nei == -1: break

                if nei not in visit:
                    stack.append(nei)
                    visit.add(nei)
                    d[nei] = d[node] + 1

                elif nei in d:
                    ans = max(ans, d[node] - d[nei] + 1)

        return ans

