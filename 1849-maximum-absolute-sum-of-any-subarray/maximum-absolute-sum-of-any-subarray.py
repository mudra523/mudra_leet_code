class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # TC: O(n), SC: 
        max_sum = min_sum = cur_max = cur_min = 0
        for n in nums:
            cur_max = max(n, cur_max + n)
            cur_min = min(n, cur_min + n)
            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)

        return max(max_sum, abs(min_sum))