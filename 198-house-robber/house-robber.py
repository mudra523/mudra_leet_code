class Solution(object):
    def rob(self, nums):
        Rob1, Rob2 = 0, 0

        for n in nums:
            Temp = max(Rob1 + n, Rob2)
            print(nums, Temp, Rob1, Rob2)
            Rob1 = Rob2
            Rob2 = Temp
        return Rob2
        