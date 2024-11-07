class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Solution 1: TC: O(n) SC O(1)
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i + 1]:
        #         return i
        # return len(nums) - 1
    
        #Solution 2: TC: O(log(n)) SC O(1)
    #     return self.search(nums, 0, len(nums) - 1)
    # def search(self, nums: List[int], l: int, r: int) -> int:
    #     if l == r:
    #         return l
    #     mid = (l + r) // 2
    #     if nums[mid] > nums[mid + 1]:
    #         return self.search(nums, l, mid)
    #     return self.search(nums, mid + 1, r)
        
        #Solution 3: TC: O(log(n)) SC O(1)
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l