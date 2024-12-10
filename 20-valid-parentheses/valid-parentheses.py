class Solution:
    def isValid(self, s: str) -> bool:
        # TC: O(n) SC: O(n)
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in mapping:
                if stack and stack[-1] == mapping[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False