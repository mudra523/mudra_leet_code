class SparseVector:
    def __init__(self, nums: List[int]):
        self.array = nums
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for n1, n2 in zip(self.array, vec.array):
            res += n1 * n2
        return res
        
#     def __init__(self, nums: List[int]):
#         self.hm = {}
#         for i, n in enumerate(nums):
#             if n != 0:
#                 self.hm[i] = n

#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec: 'SparseVector') -> int:
#         res = 0
#         for i, v in vec.hm.items():
#             if i in self.hm:
#                 res += v * self.hm[i]
#         return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)