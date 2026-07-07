class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l) # the smaller height is limiting the area
            most = max(most, area)
            if heights[l] < heights[r]:
                l += 1 # since heights[l] is limiting the area, and width decreases if we move inwards, if we move r, then the are will still be limited by l or the new heights[r] will be even smaller, so we move l
            else:
                r -= 1
        return most