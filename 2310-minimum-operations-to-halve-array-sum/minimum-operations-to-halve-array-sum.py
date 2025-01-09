class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half = sum(nums) / 2.0
        operation = 0
        heap = [ -n for n in nums]
        heapify(heap)

        while half > 0:
            num = -heappop(heap)
            num /= 2
            half -= num
            heappush(heap, -num)
            operation += 1
        return operation