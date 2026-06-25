class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)): # prefix[0] stays 1 as nothing to the left of index 0, multiplying by nothing is the same as multiplying by 1
            prefix[i] = prefix[i - 1] * nums[i - 1]
            # prefix[0] = 1
            # prefix[1] = 1 * 1 = 1
            # prefix[2] = 1 * 2 = 2
            # prefix[3] = 2 * 4 = 8

        for i in range(len(nums) - 2, -1, -1): # suffix[len(nums) - 1] stays 1 as nothing to the right of index len(nums - 1), multiplying by nothing is the same as multiplying by 1
            suffix[i] = suffix[i + 1] * nums[i + 1]

        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]

        return result