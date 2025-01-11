class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasMap = {}
        for i, n in enumerate(nums):
            temp = target - n

            if temp in hasMap:
                return [hasMap[temp], i]
            hasMap[n] = i
        # hasMap = {}

        # for i, n in enumerate(nums):
        #     temp = target - n

        #     if temp in hasMap:
        #         return [hasMap[temp], i]
        #     hasMap[n] = i