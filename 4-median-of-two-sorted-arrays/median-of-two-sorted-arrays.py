class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 #A
            j = half - i - 2 #B

            ALeft = A[i] if i >= 0 else float("-infinity")
            ARight = A[i + 1] if (i + 1) < len(A) else float("infinity")
            BLeft = B[j] if j >= 0 else float("-infinity")
            BRight = B[j + 1] if (j + 1) < len(B) else float("infinity")

            #Left partition is correct 
            if ALeft <= BRight and BLeft <= ARight:
                #odd
                if total % 2:
                    return min(ARight, BRight)
                #even
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1

