class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #pwwkew
        res = 0
        l = 0
        charSet = set()
        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
            else:
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l += 1
                l += 1
            res = max(res, r - l + 1)
        return res