class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        # highest frequency can be len(nums) as there are len(nums) elements
        elementsByFrequency = [[] for _ in range(len(nums) + 1)] # index i stores elements with frequency i
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, freq in count.items():
            elementsByFrequency[freq].append(num)
        for i in range(len(elementsByFrequency) - 1, 0, -1):
            for num in elementsByFrequency[i]:
                res.append(num)
                if len(res) == k:
                    return res


