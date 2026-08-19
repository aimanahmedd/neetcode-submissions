class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        understand:
        input: integer array of numbers
        output: integer array of integer array of numbers

        the array should be arrays of triplets that equal to 0

        [-1, 0, 1, 2, -1, 4]

        [[-1, -1, 2]. [-1, 0, 1]]

        edge cases:
            -> if none of the inputs equal to zero: return empty array
            -> if only three numbers that do eqaul zero: just return those three pairs

        match:
            two pointers method to keep track of triplets
        
        plan:
        1. sort the numbers so it's in order because once we get to all pos we
        know no triplets will be there
        2. create empty answer array
        3. for i in range(len(nums)):

            left = i+1
            right = len(nums)-1

            while right > left:
                tmp = nums[i] + nums[left] + nums[right]

                if tmp < 0:
                    left+=1
                elif tmp > 0:
                    right-=1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left+=1

                    while right > left and and nums[left] == nums[left]:
                        left+=1
            4. return answer array
                
            [-4, -1, -1, -1, 0, 1, 2]
        '''
        nums.sort() 

        answer = []

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
              continue

            left = i+1
            right = len(nums)-1

            while right > left:
                tmp = nums[i] + nums[left] + nums[right]

                if tmp < 0:
                    left+=1
                elif tmp > 0:
                    right-=1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left+=1

                    while right > left and nums[left] == nums[left-1]:
                        left+=1
        return answer
        