class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChartoCount = {}
        tChartoCount = {}
        for char in s:
            if char in sChartoCount:
                sChartoCount[char] += 1
            else:
                sChartoCount[char] = 1
        for char in t:
            if char in tChartoCount:
                tChartoCount[char] += 1
            else:
                tChartoCount[char] = 1
        return sChartoCount == tChartoCount