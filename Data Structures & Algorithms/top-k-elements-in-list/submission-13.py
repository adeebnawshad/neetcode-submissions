class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        frequency = [[] for _ in range(len(nums) + 1)] # frequency[i] stores all elements with frequency i
        numToFreq = {}
        for num in nums:
            numToFreq[num] = 1 + numToFreq.get(num, 0)
        for num, freq in numToFreq.items():
            frequency[freq].append(num)

        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res

