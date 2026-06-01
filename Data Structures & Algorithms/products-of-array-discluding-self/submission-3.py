class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Understand:
        input: integer array of numbers (nums)
        output: ineger array of numbers (output: mult of nums except for that
        current index)

        edge cases:
        array of negative, zeroes, and same number

        match:
        output should be array and use array data structure

        plan:
        1. create empty output array
        Brute Force:
        double for loop

        2. create a left multiplication side variable and right multiplication side
        variable

        3.first for loop collect all mutliplication on left side of number
            3a. output index is left num
            3b. increment left number to be nums[i] * left number

        [1, 1, 2, 8]
        4. second for loop collect all multiplication for right side of number
            3a. output[i] = output[i] * right
            3b. right = right * nums[i]
        5. return the output array
        '''

        output_array = [1] * len(nums)
        left_mult = 1
        right_mult = 1

        for i in range(len(nums)):
            output_array[i] = left_mult
            left_mult = left_mult * nums[i] #keep track of previous number

        for i in range(len(nums)-1, -1, -1):
            output_array[i] = right_mult * output_array[i]
            right_mult = right_mult * nums[i]
        return output_array
        