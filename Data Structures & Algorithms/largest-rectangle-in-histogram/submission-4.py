class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        rectangle = 0
        for i, h in enumerate(heights):
            while stack and h <= heights[stack[-1]]:
                ind = stack.pop()
                rectangle = heights[ind] * (i - (-1 if not stack else stack[-1]) - 1)
                res = max(res, rectangle)
            stack.append(i)
        while stack:
            ind = stack.pop()
            rectangle = heights[ind] * (len(heights) - (-1 if not stack else stack[-1]) - 1)
            res = max(res, rectangle)
        return res