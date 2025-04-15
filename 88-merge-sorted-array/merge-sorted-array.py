class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last index count
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()

        # l = m + n - 1

        # while m and n:
        #     if nums1[m - 1] > nums2[n - 1]:
        #         nums1[l] = nums1[m - 1]
        #         m -= 1
        #     else:
        #         nums1[l] = nums2[n - 1]
        #         n -= 1
        #     l -= 1
        
        # while n:
        #     nums1[l] = nums2[n - 1]
        #     n -= 1
        #     l -= 1

        

        