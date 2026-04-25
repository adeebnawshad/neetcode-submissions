class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        def binary_search(nums, l, r, target): # pass in l and r otherwise would need to splice array which is O(n)
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        if binary_search(nums, l, len(nums) - 1, target) != -1:
            return binary_search(nums, l, len(nums) - 1, target)
        if binary_search(nums, 0, l - 1, target) != -1:
            return binary_search(nums, 0, l - 1, target)
        return -1       
            