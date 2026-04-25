class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # replace characters with the most frequent character in the string
        count = {}
        longest = 0
        l = 0
        maxf = 0
        # check in each window if windowLen-maxF = k, if <= k, can expand the window
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            maxf = max(maxf, count[s[r]])

            # expand window → expand window → expand window
            # until it becomes invalid
            # then shrink just enough to make it valid again
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
