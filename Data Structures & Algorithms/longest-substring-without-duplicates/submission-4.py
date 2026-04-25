class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet: # remove all elements from chaSet until s[r] (the duplicate character) is gone
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
            