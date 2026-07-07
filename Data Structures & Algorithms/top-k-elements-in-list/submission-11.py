class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # highest frequency can be len(nums)
        count = [[] for _ in range(len(nums) + 1)] # count[i] stores all elements with frequenxy i
        numToFreq = {}
        for num in nums:
            numToFreq[num] = 1 + numToFreq.get(num, 0)
        for num, freq in numToFreq.items():
            count[freq].append(num)
        res = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res


