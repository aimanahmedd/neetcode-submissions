class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        understand:
        input: integer array of nums
        output: integer array nums[i] is the product of everything from original
        array except for i

        [1, 2, 4, 6]
        [48, 24, 12, 8]

        array of all the same numbers are valid
        nums in between -20 to 20
        array length between 2 and 1000

        match:
        an array - to form our final answer array

        plan:
        a solution we could do is where we get all the multiplications from the left
        side and the multiplications from the right side and multiply two products 
        together

        left side multiplication: [1, 1, 2, 8]

        right: [48 ,24, 12,8]

        1. making an empty array for both left and right
        2. get all left multiplication
            2a. for i in range(len(nums)):
                2a.a if i = 0 -> mult = 1
                2a.b else -> mult = mult *nums[i-1]
                2a.c left.append(mult)
        3. right multiplication
            3a. for i in range(len(nums), -1, -1):
                3a.a if i = -1 -> mult = 1
                else: mult * nums[i+1]
                3a.b array[i] = left[i] * mult
        return array
        '''

        left_mult = []
        answer_mult = [0] *len(nums)

        left_product = 0

        right_product = 1

        for i in range(len(nums)):
            if i == 0:
                left_product = 1
            else:
                left_product = left_product * nums[i-1]
            left_mult.append(left_product)
        
        #len(nums)-1 because we do not want an extra indice
        for i in range(len(nums)-1, -1, -1):
            answer_mult[i] = left_mult[i] * right_product
            right_product = right_product * nums[i]
        return answer_mult
