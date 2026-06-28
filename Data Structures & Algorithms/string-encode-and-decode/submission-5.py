class Solution:

    # 5#Hello5#World
    def encode(self, strs: List[str]) -> str:
        res = []
        # s = ''
        for string in strs:
            # s += str(len(string)) + '#' + string
            res.append(str(len(string)))
            res.append("#")
            res.append(string)
        return ''.join(res)
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