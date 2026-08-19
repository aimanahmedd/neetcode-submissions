class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        maxAmount = 0

        while right > left:
            width = right - left

            maxAmount = max(maxAmount, width*min(heights[right], heights[left]))

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1

        return maxAmount

        