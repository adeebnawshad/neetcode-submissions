class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num:
                product *= num
            else:
                zero_count += 1
        result = [0] * len(nums)
        if zero_count == 0:
            for i in range(len(result)):
                result[i] = product//nums[i]
        elif zero_count == 1:
            for i in range(len(result)):
                if nums[i]:
                    result[i] = 0
                else:
                    result[i] = product
        return result