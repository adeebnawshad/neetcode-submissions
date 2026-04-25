class Solution:
    def isPalindrome(self, s: str) -> bool:
        noSpaces = ''.join(char.lower() for char in s if char.isalnum())
        l = 0
        r = len(noSpaces) - 1
        while l < r:
            if noSpaces[l] != noSpaces[r]:
                return False
            l += 1
            r -= 1
        return True
