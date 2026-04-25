class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        mid = 0
        while l < r:
            mid = (l + r) // 2
            # find the index of the minimum element / pivot
            if nums[r] < nums[mid]:
                # pivot index must lie in the right
                l = mid + 1
            else:
                #pivot index must lie in the left part
                r = mid
        pivot = l
        # perform standard binary search on both parts
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        return binary_search(pivot, len(nums) - 1)