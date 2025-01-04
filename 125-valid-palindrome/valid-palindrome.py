class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution 1
        # newStr = ""
        # for string in s:
        #     if string.isalnum():
        #         newStr += string.lower()
        # return newStr == newStr[::-1]

    #Solution 2
    #     left, right = 0, len(s) - 1
    #     while left < right:
    #         while left < right and not self.alphaNum(s[left]):
    #             left += 1
    #         while right > left and not self.alphaNum(s[right]):
    #             right -= 1
    #         if s[left].lower() != s[right].lower():
    #             return False 
    #         left, right = left + 1, right - 1
    #     return True

    # def alphaNum(self, c):
    #     return (ord('A') <= ord(c) <= ord('Z') or
    #             ord('a') <= ord(c) <= ord('z') or
    #             ord('0') <= ord(c) <= ord('9'))

        # Solution 3 TC: O(n) SC: O(n)
        # Two-pointer approach
        new_str = "".join(char.lower() for char in s if char.isalnum())
        l, r = 0, len(new_str) - 1
        while l < r:
            if new_str[l] != new_str[r]:
                return False
            l += 1
            r -= 1
        return True