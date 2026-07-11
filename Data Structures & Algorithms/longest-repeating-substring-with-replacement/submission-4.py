class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #AAABABB
        # replace characters with the most frequent character in the string
        charToFreq = {}
        res = 0
        # get the max frequency in each window
        l = 0
        r = 0
        maxf = 0
        while r < len(s):
            charToFreq[s[r]] = 1 + charToFreq.get(s[r], 0)
            maxf = max(maxf, charToFreq[s[r]])
            # expand window → expand window → expand window
            # until it becomes invalid
            while (r - l + 1) - maxf > k:
                # then shrink just enough to make it valid again
                charToFreq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
                