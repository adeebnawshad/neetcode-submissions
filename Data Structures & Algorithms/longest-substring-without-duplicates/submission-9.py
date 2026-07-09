class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # pwwkew
        # l = 0, r = 2, charSet = {d, v}
        longest = 0
        l = 0
        r = 0
        charSet = set()
        while r < len(s):
            if s[r] not in charSet:
                longest = max(longest, r - l + 1)
            # r = 3
            else:
                # increment the l pointer until the window no longer contains any duplicates
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
            charSet.add(s[r])
            r += 1
        return longest
        
