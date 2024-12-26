class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k):
            pivot = random.choice(nums)

            left, right, mid = [], [], []
            for n in nums:
                if pivot < n:
                    left.append(n)
                elif pivot > n:
                    right.append(n)
                else:
                    mid.append(n)
            
            if k <= len(left):
                return quickSelect(left, k)
            
            if k > len(left) + len(mid):
                return quickSelect(right, k - len(left) - len(mid))
            
            return pivot
        return quickSelect(nums, k)