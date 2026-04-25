class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]: # s = res
        decoded = []
        i = 0
        while i < len(s): # iterate through the encoded string
            j = i
            while s[j] != '#': # continue until find a separator
                j += 1
            length = int(s[i:j]) # i should be at the beginning of the length now and j at the #
            i = j + 1
            j = i + length
            decoded.append(s[i:j]) 
            i = j
        return decoded