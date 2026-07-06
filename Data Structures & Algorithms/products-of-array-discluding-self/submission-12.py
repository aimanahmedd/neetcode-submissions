class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        understand:
        input: integer array of numbers
        output: intger array of outputs each index is product of everything except i

        [1, 2, 4, 6]

        [48, 24, 12, 8]

        order doesnt matter because it is product of everything except for i

        min length is 2
        and numbers between -20 and 20


        match:
            arrays


        
        plan:
        get all products on left side and all the products on right side and multiply together

        [1, 1, 2, 8]
        [48,24,6,1]

        [48, 24, 12, 8]


        1. create a left, right, and answer array with placeholders in all of them to represent length

        2. left prod = 1 right prod = 1

        3. create left product array first:
            3b. if index = 0 then left prod = 1
            3c. else: leftprod = left prod * nums[i-1]
            3d. left. append(leftprod)

        4. creat right product array second starting at the last index and stepping back until -1
            4b. if index = last index rightprod = 1
            4c. else rightprod = rightprod * nums[i+1]
            4d. add answer to the array

        
        5. for i in range(len(answer)):
            answer[i] = left[i] * right[i]

        return answer
        '''


        left_arr = [1] * len(nums)
        right_arr = [1]* len(nums)
        answer = [1] * len(nums)
        
        left_prod = 1
        right_prod = 1

        for i in range(len(nums)):
            if i == 0:
                left_prod = 1
            else:
                left_prod = left_prod * nums[i-1]
            left_arr[i] = left_prod


        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                right_prod = 1
            else:
                right_prod = right_prod * nums[i+1]
            right_arr[i] = right_prod

        for i in range(len(answer)):
            answer[i] = left_arr[i] * right_arr[i]

        return answer