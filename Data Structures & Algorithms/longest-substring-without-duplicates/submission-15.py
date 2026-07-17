class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #pwwkew
        longest = 0
        charSet = set()
        l = 0
        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
            else:
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l += 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest