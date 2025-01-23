class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #TC : O(n)
        res = 0
        curSum = 0
        preFixSum = { 0 : 1 }

        for n in nums:
            curSum += n
            dif = curSum - k
            res += preFixSum.get(dif, 0)
            preFixSum[curSum] = 1 + preFixSum.get(curSum, 0)
            
        return res