class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')' : '(', '}' : '{', ']' : '['}
        for c in s:
            if c in closeToOpen:
                if not stack:
                    return False
                check = stack.pop()
                if check != closeToOpen[c]:
                    return False
            else:
                stack.append(c)
        if stack: # for open brackets without a closing bracket
            return False
        return True