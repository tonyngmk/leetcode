from collections import deque

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        def addRooms(r, c):
            """
            helper function
            """
            if (r<0) or (r>=row) or (c<0) or (c>=col) or (rooms[r][c]==-1) or ((r,c) in visit):
                return
            visit.add((r,c))
            q.append((r,c))
        
        
        # init constants and data structures
        row, col = len(rooms), len(rooms[0])
        visit = set()
        q = deque()
        
        # add gates to queue
        for r in range(row):
            for c in range(col):
                if rooms[r][c] == 0:
                    visit.add((r,c))
                    q.append((r,c))

        dist = 0
        while q: # next step
            for i in range(len(q)): # traverse all gates per step
                r, c = q.popleft()
                rooms[r][c] = dist # Modify value of room
                
                addRooms(r, c+1)
                addRooms(r, c-1)
                addRooms(r-1, c)
                addRooms(r+1, c)
                        
            dist +=1

solution = Solution()
print(solution.wallsAndGates(rooms))
