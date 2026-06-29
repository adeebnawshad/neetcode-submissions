class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToCount = {}
        frequency = [[] for _ in range(len(nums))]

        for num in nums:
            numToCount[num] = 1 + numToCount.get(num, 0)

        for num, count in numToCount.items():
            frequency[count - 1].append(num)

        res = []
        for i in range(len(frequency) - 1, -1, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res