class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)

        res = 0
        for num in numSet:
            if (num - 1) not in numSet: # can be a start point
                i = num
                count = 1
                while (i + 1) in numSet:
                    i += 1
                    count += 1
                res = max(res, count)
        return res
