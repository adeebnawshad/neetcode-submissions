class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in closeToOpen:
                # empty stack means no opening bracket exists to match this one
                # top of stack must equal expected opener, since the most recently
                # opened bracket must be the next one closed (LIFO nesting)
                if not stack or stack.pop() != closeToOpen[c]:
                    return False
            else:
                stack.append(c) # opening bracket, push for later matching
        return False if stack else True # any unmatched opens left = invalid