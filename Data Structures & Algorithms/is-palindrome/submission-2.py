class Solution:
    def isPalindrome(self, s: str) -> bool:
        onlyAlNum = ''.join(c.lower() for c in s if c.isalnum())
        l = 0
        r = len(onlyAlNum) - 1
        while l < r:
            if onlyAlNum[l] != onlyAlNum[r]:
                return False
            l += 1
            r -= 1
        return True
