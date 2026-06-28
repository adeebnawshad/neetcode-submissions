class Solution:

    # 5#Hello5#World
    def encode(self, strs: List[str]) -> str:
        res = []
        # s = ''
        for string in strs:
            # s = s + str(len(string)) + '#' + string # this approach will have complexity n^2 as: iteration 1: copy 1 chunk, iteration 2: copy 2 chunks, iteration 3: copy 3 chunks... That's 1 + 2 + 3 + ... + m = O(N²) in the worst case.
            res.append(str(len(string)))
            res.append("#")
            res.append(string)
        return ''.join(res) #.join()  concatenate an iterable of strings into a single string, placing a specified separator between each element (empty string here)
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i: j])
            strs.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return strs