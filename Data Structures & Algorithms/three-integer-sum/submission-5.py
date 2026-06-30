class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            understand:
            input: integer array of numbers
            output: array of arrays that equal to zero

            [-1, 0, 1, 2, -1, -4]
            [[-1, -1, 2], [-1,0,1]]

            min length = 0
            max lenght = 1000

            smallest number is -10^5

            there is a case where we get all pos numbers -> empty array result

            if all same num that not 0, empty array


            match:
                two pointers method to focus on one number while also focusing on the others

            plan:
                1. empty answer array to store all other arrays
                2. sort out the numbers because we know once we get to al positive we are not going
                to have an answer

                3. for i in range(len(nums)):
                    3a. if i > 0 and this is the same number as prev:
                        continue
                    3b. left = i+1 right = len(nums) -1
                    3c. while right > left:
                        tmp = nums[i] + nums[left] + nums[right]

                        if tmp > 0:
                            right-=1
                        elif tmp < 0:
                            left+=1
                        else:
                            answer.append([nums[i], nums[left], nums[right]])
                            left+=1

                            while right > left and nums[left] == nums[left-1]:
                                left+=1

                        return answer
        '''


        answer = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1

            while right > left:
                tmp = nums[i] +nums[left] +nums[right]

                if tmp < 0:
                    left+=1

                elif tmp > 0:
                    right -=1
                
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left+=1

                    while right > left and nums[left] == nums[left-1]:
                        left+=1

        return answer