class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        understand:
        input: integer array of heights 
        output: max amount of water a container can store

        max amount of water = max area in the list


        [1, 7, 2, 5, 4, 7, 3, 6]

        width = distance between bars
        height = min in the left vs right bars

        O(n) not optimal! height.length -> 10000

        even with higher heigth, width might be too small

        match:
        two pointers

        plan:
        1. create a left pointer = 0 and right pointer = len(height) - 1
        2. create max_area = 0
        3. while right > left:
            check for max area:
                width = right - left and minimum between left and right

            if left is smaller move up left
            if right is smaller move up right
        4. return max area
        '''

        left = 0
        right = len(heights)-1

        maxArea = 0

        while right > left:
            width = right - left
            maxArea = max(width*min(heights[left], heights[right]), maxArea)

            #7, 

            if heights[left] <= heights[right]:
                left+=1
            elif heights[right] <= heights[left]:
                right-=1

        return maxArea