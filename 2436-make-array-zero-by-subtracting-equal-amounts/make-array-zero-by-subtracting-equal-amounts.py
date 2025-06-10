class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Brute Force Approach
        # TC: O(n^2)
        # SC: O(1)
        # count = 0
        # while any(n > 0 for n in nums):
        #     x = min(n for n in nums if n > 0)
        #     nums = [n - x if n > 0 else 0 for n in nums]
        #     count += 1
        # return count

        # Best Approach
        # TC O(n)
        # SC O(n)
        return len(set(n for n in nums if n > 0))

