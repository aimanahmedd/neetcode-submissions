class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # '''
        # max area to return
        maxArea = 0
        # two pointers, have a left pointer and a right pointer
        left = 0
        right = len(heights) - 1
        # while right is greater than the left
        while right > left:
        # maxarea = max(width* min(left, right), maxarea)
            width = right - left
            maxArea = max(width*min(heights[left], heights[right]), maxArea)

            if heights[left] <= heights[right]:
                left+=1
            elif heights[right] <= heights[left]:
                right-=1
        return maxArea
    #[1,7,2,5,4,7,3,6]
        # if left is smaller, move left up
        # if right is smaller move right down

        # outside of while loop, return the max area


        # '''
        