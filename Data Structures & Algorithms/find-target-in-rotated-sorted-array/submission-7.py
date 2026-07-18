class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find deflection point / minimum then do binary search on each half
        # if the array is rotated then we have a left sorted portion and a right sorted portion, right sorted portion has the minimum element
        l = 0
        r = len(nums) - 1
        while l < r: # the invariant we're maintaining is min exists in nums[l:r]
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                # mid in left sorted portion
                l = mid + 1 # as min in right sorted portion
            else:
                # mid in right sorted portion so min at r or left of r (as min is the first element in the right sorted portion) (this deals with the non-rotated case too)
                r = mid
        minIdx = l

        def binary_search(l, r, target):
            while l <= r: # = because of single element array/ portion of array, we still need to check that
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        left_result = binary_search(0, minIdx - 1, target)
        if left_result != -1:
            return left_result
        else:
            return binary_search(minIdx, len(nums) - 1, target)

