class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: # avoid duplicates for i (need i > 0 as i starts at 0)
                continue
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k: # prevent pointers crossing - There are no more pairs left to check.
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]: #skip duplicates and j < k prevents from making j go out of bounds
                        j += 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return result
