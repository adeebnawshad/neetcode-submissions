class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # highest frequency can be len(nums)
        # nums = [1,2,2,3,3,3], k = 2
        # {1 : 1}, {2 : 2, 3: 3}
        # len(nums) = 6
        # freq[i] stores elements that appear i times
        # freq[5] = []
        # freq[4] = []
        # freq[3] = [3]
        # freq[2] = [2]
        # freq[1] = [1]
        freq = [[] for _ in range(len(nums) + 1)]
        numToCount = {}
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

            
        
