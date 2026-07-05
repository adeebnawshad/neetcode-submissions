class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):
            target = -nums[i]
            if i > 0 and nums[i - 1] == nums[i]: # nums[i] is the same value as nums[i-1], that means I already fully explored every possible pair (l, r) for that value in the previous iteration — because the array is sorted, nums[i-1] == nums[i] guarantees the entire remaining subarray to the right looks identical too.
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # since i stays the same, if the value of nums[l] stays the same, we'd get the same value for nums[r] again as target is the same so nums[r] = target - nums[l]
                    while l < r and nums[l - 1] == nums[l]: # we check l -1 as l - 1 is the index of the value we just used in the accepted triplet (as we just did l += 1), and l is the new candidate
                        l += 1
        return res