class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        understand:
        input: integer array of nums
        output: array of numbers but i has to be the product of everything except itself

        [1, 2, 4, 6]
        [48, 24, 12, 8]

        array length between 2 to 1000
        -20 to 20

        match:
            array (collect products on left side and collect products on the right side)


        plan:

        [1, 1, 2, 8]
        [ 48, 24,6,1]

        1. set a variable of the left & right product to 1 and have an empty array to keep track of all left side
        products and right side array(placeholders)
        
        answer array with placeholders

        2. for i in range(len(index)):
            2a. if i == 0:
                left_prod = 1
            2b. else:
                left_prod = left_prod * num[i-1]
            2c. left array . append(left_prod)


            [1, 1, 2, 8]

        3. for i range(len(num)-1, -1, -1):
            3a. if i == len(num)-1:
                right_prod = 1
            3b. else:
                right_prod = right_prod * num[i+1]
            3c. right_arr[i] = right_prod

        4. for i in answer:
            answer[i] = left_prod[i] * right_prod[i]

        5. return answer

        '''

        left_prod = 1
        right_prod = 1

        left_arr = []
        right_arr = [1]*len(nums)

        answer = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                left_prod = 1
            else:
                left_prod = left_prod * nums[i-1]
            left_arr.append(left_prod)
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                right_prod = 1
            else:
                right_prod = right_prod * nums[i+1]
            right_arr[i] = right_prod

        for i in range(len(nums)):
            answer[i] = left_arr[i] * right_arr[i]
        return answer