class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        understand:
        input: integer array of heights, heights[i] = height
        output: max area to store water

        [1, 7, 2, 5, 4, 7, 3, 6]
        -> 36 the most amount water than can be stored

        does not need to be sorted!

        smallest is 2 and largest height is 100000
        heights can be betweem 0 and 10000

        match:
            two pointers method to keep track of basically container for water

        plan:
        1. left and right pointer, left is first index right is last index
        2. maxArea = 0
        3. while right > left:
            width = right - left (distance between two bars)

            maxArea = max(maxArea, width* min(heights[right], heights[left]))

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        4. return maxArea
        '''
        left, right = 0, len(heights)-1
        maxArea = 0

        while right > left:
            width = right - left

            maxArea = max(maxArea, width*min(heights[right], heights[left]))

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return maxArea


        