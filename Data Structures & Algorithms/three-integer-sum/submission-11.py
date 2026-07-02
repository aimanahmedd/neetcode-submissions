class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        understand:
        input: integer array of numbers
        output: array of array of numbers which equal 0

        [-1, 0, 1, 2, -1, 4]

        [[-1, -1, 2], [-1, 0, 1]]

        - if no triplets, return empty array
        - if all three equal 0, return that array

        array min is 3

        match:
            two pointers method


        plan:
        1. create an empty array variable which will store all the different array combinations
        2. sort the numbers
        3. for loop with index:
            3b. if i > 0 and nums[i] == nums[i-1] -> continue (move on to the next value)

            3c. make a left pointer eqaul to i+1 and right pointer last num in array

            3d. while right > left:
                make a tmp variable that if the sum of all three indexes
                3d.a if tmp > 0 reduce right
                3d.b if tmp < 0 increase left
                3d.c else append this sum to answer array and increase left pointer

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