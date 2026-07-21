class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set()
        for num in nums:
            numSet.add(num)
        for num in numSet:
            if (num - 1) not in numSet:
                count = 1
                while (num + count) in numSet:
                    count += 1
                longest = max(longest, count)
        return longest