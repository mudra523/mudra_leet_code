class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = [0] * 10
        for digit in num:
            count[int(digit)] += 1

        half = []
        mid = ''

        for digit in range(9, -1, -1):  # Corrected range
            if count[digit] % 2 == 1 and not mid:
                mid = str(digit)
            half.extend([str(digit)] * (count[digit] // 2))

        while half and half[0] == '0':
            half = half[1:]

        half_new = ''.join(half)

        if half_new or mid:
            return half_new + mid + half_new[::-1]
        return '0'
