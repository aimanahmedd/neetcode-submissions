class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left
            area = width * min(heights[left], heights[right])

            if area > result:
                result = area

            if heights[left]<heights[right]:
                left+=1
            elif heights[right] < heights[left]:
                right-=1
            else:
                left+=1
        return result
        