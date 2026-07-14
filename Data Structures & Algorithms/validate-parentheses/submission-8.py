class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in closeToOpen:
                if not stack or stack.pop() != closeToOpen[c]: # first close bracket must match the last open bracket added to the stack as we close the latter open brackets before the fromer open brackets
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True