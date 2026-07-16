class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in closeToOpen:
                if not stack or stack.pop() != closeToOpen[c]: # check not stack in case there's nothing in the stack which means no opening bracket for the closed bracket # first close bracket must match the last open bracket added to the stack as we close the latter open brackets before the former open brackets
                    return False
            else:
                stack.append(c)
        return False if stack else True