class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # replace characters with the most frequent character in the string
        longest = 0
        count = {}
        l = 0
        # get the max frequency in each window
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            maxFreq = max(count.values())
            # expand window → expand window → expand window
            while (r - l + 1) - maxFreq > k: # until it becomes invalid
                # then shrink just enough to make it valid again
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest