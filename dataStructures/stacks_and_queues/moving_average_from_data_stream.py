class MovingAverage(object):

#     # Approach 1: Array
#     def __init__(self, size):
#         """
#         :type size: int
#         """
#         self.size = size
#         self.queue = []

#     def next(self, val):
#         """
#         :type val: int
#         :rtype: float
#         """
#         self.queue.append(val)
#         return sum(self.queue[-self.size:]) / min(self.size, len(self.queue))
        
#     # Approach 2: Deque
#     from collections import deque
#     def __init__(self, size):
#         """
#         :type size: int
#         """
#         self.size = size
#         self.queue = deque()
#         self.window_sum = 0
#         self.count = 0
        

#     def next(self, val):
#         """
#         :type val: int
#         :rtype: float
#         """
#         self.count+=1
#         self.queue.append(val)
#         tail = self.queue.popleft() if self.count > self.size else 0
#         self.window_sum = self.window_sum - tail + val
#         return self.window_sum / min(self.size, self.count)

    # Approach 3: Circular queue with array
    from collections import deque
    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = self.count = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.count+=1
        # for current iteration
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # for next iteration
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)
        
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
