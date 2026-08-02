class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        understand:
            input: integer array of numbers
            output: indices of nums that nums[i] and nums[j] == target

            [3, 4, 5, 6] target was 7
            -> [0, 1] 3+4=7

            [4, 5, 6] target 10
            -> [0, 2] 4+6=10

            always a solution never an empty array

            match:
                use hashmap to store numbers we come across 

            plan:
                1. hashmap to store all previous numbers

                2. loop for i in range(len(nums)):
                    if target-nums[i] in hash:
                        return [hash[target-nums[i]], i]
                    else:
                        hash[nums[i]] = i

        '''
        prevNums = {}

        for i in range(len(nums)):
            if target-nums[i] in prevNums:
                return [prevNums[target-nums[i]], i]
            else:
                prevNums[nums[i]] = i
        