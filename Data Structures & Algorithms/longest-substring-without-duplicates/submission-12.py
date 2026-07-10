class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # pwewkew # longest = 3
        # l = 0 # r = 0
        longest = 0
        l = 0
        charSet = set()
        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
                longest = max(longest, r - l + 1)
            else:
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l += 1
                l += 1
        return longest