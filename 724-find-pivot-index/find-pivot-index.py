class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = 0
        total = sum(nums)

        for i in range(len(nums)):
            sumRight = total - nums[i] - sumLeft
            if sumLeft == sumRight:
                return i
            sumLeft += nums[i]
        return - 1