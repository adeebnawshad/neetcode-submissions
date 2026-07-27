class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(area, res)
            if heights[l] < heights[r]: # this means heights[l] is limiting the area
                # so if we move r inwards, the width decreases by 1 and either height[l] is still gonna limit the area or something else smaller than heights[l] will limit the area, so the area will get smaller
                # so we must move l inwards
                l += 1
            else:
                r -= 1
        return res