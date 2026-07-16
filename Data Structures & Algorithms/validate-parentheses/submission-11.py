class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in closeToOpen:
                if not stack or stack.pop() != closeToOpen[c]: # last open bracket is the first opening bracket to close
                    return False
            else:
                stack.append(c)
        return False if stack else True