class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for c in s:
            if c in closeToOpen:
                if not stack:
                    return False
                if stack.pop() != closeToOpen[c]:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True