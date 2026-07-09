class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # pwwkew
        # l = 0, r = 2, charSet = {p, w}
        longest = 0
        l = 0
        r = 0
        charSet = set()
        while r < len(s):
            if s[r] not in charSet:
                longest = max(longest, r - l + 1)
            else:
                # increment the l pointer until the window no longer contains any duplicates
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l += 1
                l += 1
            charSet.add(s[r])
            r += 1
        return longest
        
