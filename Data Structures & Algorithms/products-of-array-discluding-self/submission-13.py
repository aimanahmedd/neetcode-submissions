class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            understand:
            input: integer array of numbers
            output: integer array product[i] is every product
            except itself

            [1, 2, 4, 6]

            [48, 24, 12, 8]

            match:
                using arrays

            plan:
                1. make an array of right left and product
                filled with placeholders inside of the array
                2. make left product and right product
                3. get all left product (use for loop with index)
                    3a. if first number in array is i=0, left prod
                    equals to 1
                    3b. else left prod is left prod * prev num
                4. get all right product range(len(nums)-1, -1, -1)
                    4a. if last index, right prod equals one
                    4b. else right prod is right prod * num ahead
                5. loop through answer and multiply left with right
                for each index
        '''
        left_arr = [1] * len(nums)
        right_arr = [1] *len(nums)
        product_arr = [1]*len(nums)

        left_prod = 1
        right_prod = 1

        for i in range(len(nums)):
            if i == 0:
                left_prod = 1
            else:
                left_prod = left_prod *nums[i-1]
            left_arr[i] = left_prod
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                right_prod = 1
            else:
                right_prod = right_prod * nums[i+1]
            
            right_arr[i] = right_prod

        for i in range(len(product_arr)):
            product_arr[i] = left_arr[i] * right_arr[i]
        
        return product_arr

        