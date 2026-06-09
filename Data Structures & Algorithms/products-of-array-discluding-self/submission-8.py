class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        understand:
        input: integer array of numbers ([1,2,3,4])
        output: array of numbers but output[i] should be the product
        of everything except nums[i]


        [1, 2, 4, 6]
        [48, 24, 12, 8]

        numbers go from -20 to 20
        never an empty array (always a min of 2)
        an array with all same numbers allowed

        match:
            no hashmap because we don't need to store or pull 
            anything out of this
        
        plan:
        get all the left side numbers and get all the right side
        numbers and multiply them together

        [1, 2, 4, 6]


        [1, 1, 2, 8]

        [1, 6, 24, 48]

        [ 48 24 12 8]

        1. create a variable initializing left_product and right_product along with left array and answer array
        2. go through left side and increase left product along with appending to left arrat
        3. to get right product start at the end and step by -1
            3a. add right mult * num[i] immediately to answer array
            3b. increase right mult * left array[i]

        '''
        left_prod_array = []
        answer = [1]*len(nums)

        left_prod = 1
        right_prod = 1

        for i in range(len(nums)):
            if i == 0:
                left_prod = 1
            else:
                left_prod = left_prod * nums[i-1] #why i-1 over here??
            left_prod_array.append(left_prod)

        for i in range(len(nums)-1, -1, -1):
            answer[i] = right_prod * left_prod_array[i]
            right_prod = right_prod * nums[i]

        return answer