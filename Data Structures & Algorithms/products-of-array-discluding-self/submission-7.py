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
        if zero_count > 1:
            return result
        for i in range(len(result)):
            if zero_count:
                if nums[i] == 0:
                    result[i] = product
            else:
                result[i] = product//nums[i]
        return result