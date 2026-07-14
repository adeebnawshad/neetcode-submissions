class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #AAABABB, k = 1
        res = 0
        maxf = 0
        l = 0
        r = 0
        # we want to replace some other characters with the most frequent character
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # expand the window until it becomes invalid (difference between length and count of most frequent character more than k)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res