class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        understand:
        input: integer array nums
        output: array, where output[i] is the product of every number except
        for nums[i]

        [1, 2, 4, 6]
        [48, 24, 12, 8]

        always fit in a 32 bit integer
        2<= nums.length <= 100000
        -30 <= nums[i] <= 30

        match:
            arrays 
        
        plan:
        1. create a left, right, and answer array to store products for each side 
        of i
        2. create two vars to keep track of left product and right product
        3. for i in range(len(nums)):
            if i > 0:
                leftProd = leftProd * nums[i-1]
            
            leftArr[i] = leftProd
        4. for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                rightProd = rightProd * nums[i+1]
            rightArr[i] = rightProf

        5. for i in range(len(answer)):
            answer[i] = leftArr[i] * rightArr[i]
        6. return answer
        '''
        leftArr, rightArr, answerArr = [1] * len(nums), [1]* len(nums), [1]* len(nums)
        #lA=[1, 1, 1, 1] rA=[1, 1, 1, 1] aA=[1, 1, 1, 1]

        leftProd, rightProd = 1, 1

        for i in range(len(nums)):
            if i == 0:
                leftProd = 1
            else:
                leftProd = leftProd *nums[i-1]
            leftArr[i] = leftProd

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                rightProd = 1
            else:
                rightProd = rightProd * nums[i+1]

            rightArr[i] = rightProd
        
        for i in range(len(answerArr)):
            answerArr[i] = leftArr[i] * rightArr[i]
        
        return answerArr
