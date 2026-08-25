class Solution:

    def encode(self, strs: List[str]) -> str:
        5#Hello5#World
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)

        # "Encode runs in O(m+n) time and space, where m is the total number of characters across all strings and n is the number of strings. I iterate through each of the n strings once, and for each one I do O(1) extra work for the length-prefix and delimiter, plus O(L) work to append its L characters. Summed over all strings that's O(m) for the content and O(n) for the per-string overhead, so O(m+n) total. Same reasoning for space — I'm building an output string that has to hold all m characters plus n digit-tags and n delimiters."
    def decode(self, s: str) -> List[str]:
        res = []
        # find '#'
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # get length
            length = int(s[i : j])
            # go length steps forward
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

        #"Decode is also O(m+n) time. It might look like nested loops could mean O(N²), but the inner while-loop pointer j never resets — it only moves forward — so across the whole function the two pointers together make a single linear pass over the string. That's the standard two-pointer argument for why this is linear, not quadratic.

#For space, I'd distinguish output space from auxiliary space. The output itself — the list of decoded strings — is O(m+n), same reasoning as before. But if you're asking about extra space I use beyond the output, that's O(1) — just a few pointer variables (i, j, length) that don't grow with input size."

#But res isn't one big string — it's a list of n separate string objects. And holding n items in a list costs space for n references/pointers, regardless of how long or short each string is. Even if every string were empty (m=0), a list of n items still needs O(n) space just to hold those n slots/pointers.

#So the breakdown is:

#O(m) for the actual character content across all the decoded strings
#O(n) for the list structure itself — n entries, n string-object overheads

#Total: O(m+n), not just O(m).

#This is actually the same reasoning as encode, just flipped:

#In encode, the n comes from the n digit-tags and n # delimiters you explicitly add into the single output string.
#In decode, the n comes from the fact that the output is n distinct objects in a list rather than one joined string.
