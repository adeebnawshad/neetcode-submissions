class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            most = max(most, area)
            # move the shorter pointer inwards because the shorter height is the one limiting our area.
            # the weidth will decrease by 1 if we move inwards so if we move the taller pointer inwards we get a smaller area as the width decreases
            if heights[l] < heights[r]:
                l += 1 
            else:
                r -= 1
        return most