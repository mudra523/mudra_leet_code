class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 1 
        # if k == len(nums):
        #     return nums
        
        # count = Counter(nums)
        # return heapq.nlargest(k, count.keys(), key = count.get)

        # Solution 2 TC: O(K logn)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, value in count.items():
            freq[value].append(key)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

       
    
       