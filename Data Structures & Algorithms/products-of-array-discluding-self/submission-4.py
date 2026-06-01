class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        understand:
        inputs: integer array nums (example: [1, 2, 3, 4])
        output: array of numbers ([24, 12, 8, 6])

        there is still a chancce for an array to have all the same numbers, negatives, 
        and zeroes. no possible chance of having array of length 1 or 0
        -> numbers fall between -20 and 20
        
        data structure: array

        plan:
        get product of left side of the number and get the product of the right side of
        number
        1. empty array for output
        2. set a variable to keep track of left product (left_product)
        3. set a varaible to keep track of right product (right_product)
        4. for loop i in range(len(nums)):
            4a. output[i] = left_product
            4b. left_product = left_product * nums[i]
            [1, 1, 2, 8]
        5. for i in range(len(nums)-1, -1, -1):
            5a. output[i] = output[i] * right_product
            5b. right_product = right_product * nums[i]

        [48 ,24, 12,8]


        []
        '''

        output = [1] * len(nums)
        left_product = 1 #keep track of products to left of nums[i]
        right_product = 1 #keep track of products to right of nums[i]

        for i in range(len(nums)):
            output[i] = left_product
            left_product = left_product * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * right_product
            right_product = right_product * nums[i]
        return output         