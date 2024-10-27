class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        sum = 0
        for weight in w:
            sum += weight
            self.prefix_sums.append(sum)
        self.total_sum = sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        # run a linear search to find the target zone   TC O(N)
        # for i, sum in enumerate(self.prefix_sums):
        #     if target < sum:
        #         return i
        
        # run a binary search to find the target zone  TC O(log N)
        low , high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else: high = mid
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()