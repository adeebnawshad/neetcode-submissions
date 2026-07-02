class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # highest frequency can be len(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        # freq[1] = [1], freq[2] = 2, ...
        numToCount = {}
        # {1 : 1}, {2 : 2}, ...
        for num in nums:
            numToCount[num] = 1 + numToCount.get(num, 0)
        for num, count in numToCount.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
        
