class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        understand:
        input: integer array nums
        output: new integer array output[i] should be product
        of everything except for nums[i]

        [1, 2, 4, 6]

        [48, 24, 12, 8]

        match:
            array

        plan:
            1. have a left array, right array, and answer array placeholders to 
            keep track of the products in the left and right
            2. leftmult variable and rightmult variable
            3. for i in range(len(nums)):
                if i == 0:
                    leftmult = 1
                else:
                    leftmult = leftmult * prev num
                leftarray[i] = leftmult

                [1, 1, 2, 8]
            4. for i in range(len(nums)-1, -1, -1):
                if i == len(nums)-1:
                    rightmult = 1
                else:
                    rightmult = rightmult * nums[i+1]
                rightarray[i] = rightmult
            5.for i in range(len(answers)):
                answer[i] = left[i] * right[i]

            return answer
        '''
        leftArr, rightArr, answerArr = [1]*len(nums), [1]*len(nums), [1]*len(nums)

        leftProd = 1
        rightProd = 1

        for i in range(len(nums)):
            if i > 0:
                leftProd = leftProd * nums[i-1]
            leftArr[i] = leftProd
        
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                rightProd = rightProd * nums[i+1]
            rightArr[i] = rightProd

        for i in range(len(answerArr)):
            answerArr[i] = leftArr[i] * rightArr[i]
        return answerArr

        