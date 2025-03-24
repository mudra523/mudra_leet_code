class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Base case
        if not s and len(s) == 1:
            return s

        def palLength(s: str, l: int, r: int):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        maxLenSub = ''
        for i in range(len(s)):
            odd = palLength(s, i, i)
            even = palLength(s, i, i + 1)
            if len(odd) > len(maxLenSub):
                maxLenSub = odd 
            if len(even) > len(maxLenSub):
                maxLenSub = even
         
        return maxLenSub