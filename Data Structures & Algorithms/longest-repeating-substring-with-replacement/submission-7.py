class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #AAABABB
        # replace different characters with the most frequent character in the string
        count = [0] * 26
        res = 0
        # get the max frequency in each window
        l = 0
        r = 0
        maxf = 0
        while r < len(s):
            count[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, count[ord(s[r]) - ord('A')])
            # expand window → expand window → expand window
            # until it becomes invalid (length - maxf > k) - this means we'd need to replace more than k characters to make all the characters the same
            while (r - l + 1) - maxf > k:
                # then shrink just enough to make it valid again
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
                