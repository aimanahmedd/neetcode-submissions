class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 #first element in the array
        right = len(heights) - 1 #last element in the array
        maxArea = 0

        while right > left:
            width = right - left #total distance between two points
            tmpArea = width * min(heights[right], heights[left])

            if tmpArea > maxArea:
                maxArea = tmpArea

            if heights[right] <= heights[left]:
                right-=1
            else:
                left+=1
        return maxArea





        '''
        left = 0
        right = last index of the area

        maxArea = 0
        while right is bigger than the left:
            area = (right - left) * min height

            if area > maxArea:
                maxArea = area
            
            if right <= left:
                right-=1
            else:
                left+=1
        return maxArea
        '''

        