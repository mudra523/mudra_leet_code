class MovingAverage:
    # Approach 2: Array or List
    # Solution 2 TC: O(1), SC: O(N) where N is the size of the moving window.
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        
        tail = self.queue.popleft() if self.count > self.size else 0
        self.window_sum = self.window_sum + val - tail
        return self.window_sum / min(self.count, self.size)
    
    # Approach 1: Array or List
    # Solution 1 TC: O(N.M), SC: O(M)
#     def __init__(self, size: int):
#         self.size = size
#         self.queue = []

#     def next(self, val: int) -> float:
#         size, queue = self.size, self.queue
#         queue.append(val)
        
#         window_sum = sum(queue[-size:])
#         return window_sum / min(len(queue), size)
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)