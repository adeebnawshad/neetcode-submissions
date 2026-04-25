class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        for num in nums:
            if num in numFreq:
                numFreq[num] += 1
            else:
                numFreq[num] = 1
        
        freqToNum = [[] for _ in range(len(nums) + 1)]
        for num, freq in numFreq.items():
            freqToNum[freq].append(num)

        res = []
        for i in range(len(freqToNum) - 1, 0, -1):
            for num in freqToNum[i]:
                res.append(num)
                if len(res) == k:
                    return res