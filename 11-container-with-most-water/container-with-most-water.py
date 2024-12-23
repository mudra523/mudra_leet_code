class Solution:
    def maxArea(self, height: List[int]) -> int:
        # TC: O(n) SC: O(1)
        left, right = 0, len(height) - 1
        maxArea = 0

        while left < right:
            maxArea = max((right - left) * min(height[left], height[right]), maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
        