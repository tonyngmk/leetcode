class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost = 0
        last7, last30 = collections.deque(), collections.deque()

        for day in days:
            # clear unneeded space
            while last7 and last7[0][0] + 7 <= day: last7.popleft()
            while last30 and last30[0][0] + 30 <= day: last30.popleft()
            
            # calculate 7, 30 cost in current step
            last7.append((day, cost + costs[1]))
            last30.append((day, cost + costs[2]))

            # calculate minimum cost in current step
            cost = min (
                cost + costs[0],
                last7[0][1],
                last30[0][1]
            )

        return cost
