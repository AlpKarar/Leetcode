class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        result = 0

        while l < r:
            cur = (r - l) * min(height[l], height[r])
            result = max(result, cur)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return result