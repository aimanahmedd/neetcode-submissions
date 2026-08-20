class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        understand:
        input: integer array of numbers
        output: array of integer array of triplets

        [-1, 0, 1, 2, -1, -4]
        -> [[-1, -1, 2], [-1, 0, 1]] = triplets add to 0!

        [0, 1, 1] -> []

        [0, 0, 0] -> [[0,0, 0]]

        match:
            two pointer method

        plan:
        1. answer = []
        2. for i in range(len(nums)):
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

        3. return answer
        '''
        nums.sort() 
        answer = []

        #[-4, -1, -1, -1, 0, 1, 2]

        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0:
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

                    while nums[left] == nums[left-1] and right > left:
                        left+=1
        return answer

        