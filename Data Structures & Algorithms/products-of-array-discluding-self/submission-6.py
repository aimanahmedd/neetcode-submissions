class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        input: array of nums
        output: array( of nums num[i] should be the product of everything
        except for nums[i]

        match:
            array


        plan:
        1. create an empty left output array and a nums array filled with placeholder
        2. left_mult var and right_mult var set to 1

        3. for loop to get all left side products
            3a. for i in range(len(nums)):
                3a.a if i = 0: left_mult = 1
                3a.b else: left_mult = left_mult * nums[i]
                3a.c left_arr.append(left_mult)

        4. for loop to get all right side products
            3a. for i in range(len(nums)-1, -1, -1):
                3a.a right_mult = right_mult * nums[i]
                3a.b answer[i] = right*mult *left[i]
        return answer
        '''

        left_output_arr = []
        answer_output_arr = [1] * len(nums)

        left_mult = 1
        right_mult = 1

        for i in range(len(nums)):
            if i == 0:
                left_mult = 1
            else:
                left_mult = left_mult * nums[i-1]
            left_output_arr.append(left_mult)


        for i in range(len(nums)-1, -1, -1):
            answer_output_arr[i]  = right_mult * left_output_arr[i]
            right_mult = right_mult* nums[i]
        return answer_output_arr
