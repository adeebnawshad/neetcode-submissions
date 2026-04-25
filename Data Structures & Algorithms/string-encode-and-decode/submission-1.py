class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            n = len(string)
            s = s + str(n) + '#' + string
        return s
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                length = int(s[i])
                if s[i + 1].isdigit():
                    length = int(s[i : i + 2])
                    if s[i + 2].isdigit():
                        length = int(s[i : i + 3])
            if len(str(length)) == 1:
                i += 2
            elif len(str(length)) == 2:
                i += 3
            else:
                i += 4
            string = ""
            for j in range(length):
                string = string + s[i]
                i += 1
            result.append(string)
        return result