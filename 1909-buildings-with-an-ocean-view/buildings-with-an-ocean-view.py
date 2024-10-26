class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = []
        for i in range(n):
            while res and heights[res[-1]] <= heights[i]:
                res.pop()
            res.append(i)
        return res