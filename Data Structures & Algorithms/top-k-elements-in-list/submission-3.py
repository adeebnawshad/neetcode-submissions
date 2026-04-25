class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map - number to frequency
        numToFreq = {} # {1:1, 2:2, 3:3}
        for num in nums:
            if num in numToFreq:
                numToFreq[num] += 1
            else:
                numToFreq[num] = 1
        # bucket list for each frequency
        freqBucketList = [[] for _ in range(len(nums) + 1)]
        for num, freq in numToFreq.items():
            freqBucketList[freq].append(num)
        # iterate bucket list from the end and append to resultd list, return when len = k
        res = []
        for i in range(len(freqBucketList) - 1, 0, -1):
            for n in freqBucketList[i]:
                res.append(n)
                if len(res) == k:
                    return res