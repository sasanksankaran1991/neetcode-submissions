class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        for x in range(len(heights)):
            for y in range(x, len(heights)):
                val = min(heights[x], heights[y])*(y-x)
                if val > max_val:
                    max_val = val

        return max_val