class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        charFrequencyToStrings = defaultdict(list) # It's a dictionary that automatically creates a default value when you access a key that doesn't exist yet. defaultdict(list) means the default value is an empty list []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            charFrequencyToStrings[tuple(count)].append(s)

        return list(charFrequencyToStrings.values())
            