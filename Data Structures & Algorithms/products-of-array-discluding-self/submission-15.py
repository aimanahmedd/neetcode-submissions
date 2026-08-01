class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        understand:
        input: integer array of nums
        output: new integer array where i is the product of everything except
        for nums[i]

        [1, 2, 4, 6]

        [48, 24, 12, 8]

        always a solution
        max length is 20 -> o(n) time works! :)

        match:
            array

        plan:
        1. make an array for left products, right product, and answer array
        2. make a variable for left product and right product (both should be 1)
        3. for i in range(len(nums)):
            if i == 0:
                left product = 1
            else:
                left product = left product * nums[i-1]
            left products.append(left product)
        4. for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                right product = 1
            else:
                rigth product = right product * nums[i+1]
            rightproducts[i] = right product
        5. for i in range(len(answer)):
        answer[i] = leftproducts[i] * rightproducts[i]
        6. return answer
        '''
        leftProds, rightProds, answerArr = [1] * len(nums), [1]*len(nums), [1]*len(nums)

        leftProduct, rightProduct = 1, 1

        for i in range(len(nums)):
            if i > 0:
                leftProduct = leftProduct * nums[i-1]

            leftProds[i] = leftProduct
        
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                rightProduct = rightProduct * nums[i+1]
            rightProds[i] = rightProduct
        
        for i in range(len(answerArr)):
            answerArr[i] = leftProds[i] * rightProds[i]

        return answerArr