class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCharToCount = {}
        tCharToCount = {}
        for i in range(len(s)):
            sCharToCount[s[i]] = 1 + sCharToCount.get(s[i], 0)
            tCharToCount[t[i]] = 1 + tCharToCount.get(t[i], 0)

        return sCharToCount == tCharToCount