class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for word1 in words:
            for word2 in words:
                if word1 != word2 and word2 in word1:
                    result.add(word2)
        return list(result)