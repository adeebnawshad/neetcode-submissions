class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            # this if condition is not necessary because of the standalone n in the calculations of curMax and curMin
            #if n == 0:
            #    curMin, curMax = 1, 1
            #    continue

            if n < 0:
                curMax, curMin = curMin, curMax

            curMax = max(n, curMax * n)
            curMin = min(n, curMin * n)

            res = max(res, curMax)
        return res

        
    

