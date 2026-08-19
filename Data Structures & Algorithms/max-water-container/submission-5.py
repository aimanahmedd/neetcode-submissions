class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        understand:
        input: integer array of heights
        output: max area that water can be stored in between two buckets

        [1, 7, 2, 5, 4, 7, 3, 6]

        output: 36 max amount of water that can be stored
        least amount of height is 2 max is 100k

        we can have instances where height may be 0 upto 10000

        [0, 10000]

        match:
            two pointers find the max on both ends!

        plan:
        1. maxAmount = 0
        2. for i in range(len(heights)):
            left = i
            right = len(heights)-1

            while right > left:
                width = right - left

                maxAmount = max(maxAmount, width*min(right, left))

                if heights[left] < heights[right]:
                    left+=1
                else:
                    right-=1
        3. return maxAmount
        '''
        maxAmount = 0


        left = 0
        right = len(heights)-1

        while right > left:
            width = right - left

            maxAmount = max(maxAmount, width*min(heights[right], heights[left]))

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return maxAmount
        