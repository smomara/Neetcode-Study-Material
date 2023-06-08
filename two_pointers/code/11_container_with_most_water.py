class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxArea = (r - l) * min(height[r], height[l])

        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            maxArea = max(maxArea, (r-l)*min(height[r],height[l]))
        
        return maxArea
