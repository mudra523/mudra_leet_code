class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # TC : O(4^n)
        res = []
        digitToChar = {'2': 'abc',
                        '3': 'def',
                        '4': 'ghi',
                        '5': 'jkl',
                        '6': 'mno',
                        '7': 'pqrs',
                        '8': 'tuv',
                        '9': 'wxyz'}

        def backTracking(i, curStr):
            if len(digits) == len(curStr):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backTracking(i + 1, curStr + c)
        
        if digits:
            backTracking(0, '')

        return res 