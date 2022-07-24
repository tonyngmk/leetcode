from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        
        def exploreNext(node):
            for i in range(4):
                for j in (-1, 1:
                    x = int(node[i])
                    x = (x + j) % 10
                    yield node[:i] + str(x) + node[i+1:]
        
        q = deque([('0000', 0)])
        seen = {'0000'}
        while q:
            node, depth = q.popleft()
            if node == target: return depth
            if node in deadends: continue
            for i in exploreNext(node):
                if i not in seen:
                    seen.add(node)
                    q.append((node, depth+1))
                    
        return -1