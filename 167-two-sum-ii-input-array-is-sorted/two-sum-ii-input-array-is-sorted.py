class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l, r = 0, len(n) - 1

        while l < r:
            total = n[l] + n[r]

            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []