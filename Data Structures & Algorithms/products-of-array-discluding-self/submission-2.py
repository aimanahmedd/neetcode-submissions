class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Understand:
        input: array of numbers
        output: array of numbers (index should be all nums multiplied except self)

        edge cases:
        negatives and zeroes are allowed
        32-bit integers
        never an array of just 1 number

        match:
        use an array

        plan:
        brute force solution:
        double for loop

        1. making the output array
        2. making a left multiplication side variable and a right multiplication side
        variable
        3. do a for loop for i in range of length of nums
            3a. get the multiplication for all the numbers to the left
            3b. if index to left is less than 0, automatically make it one
            3c. left mult keeps track of what num in output array will be
        4. for a for loop for i in range of length of nums - 1 and basically start
        from last index all the way up
            4a. answer array index = nums index * right nult
            4b. change right mult to eqaual to right*current num in idnex
        5. return answer array

        [1, 2, 4, 6]

        [1, 1, 2, 8]

        [12 ,8]
        '''

        output_array = [1] *len(nums)
        left_val = 1 #to keep track of previous left number mult
        right_val = 1 #to keep track of previous right number mult

        for i in range(len(nums)):
            output_array[i] = left_val
            left_val = left_val * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            output_array[i] = output_array[i] * right_val
            right_val = right_val * nums[i]

        return output_array

        