class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        understand:
        input: integer array of numbers, target of what we want
        output: array of indices (where numbers eqaul to target)

        edge cases:
        always a valid answer
        doesn't matter if positive or negative

        match:
            hashmap: to keep track of previous numbers in array

        plan:
        1. make an empty hashmap for all prev nums
        2. do a for loop with indices
            2a. target - current numbers
            2b. if that answer is in our hashmap -> return array of both indices
            2c. else just add the current number and index to the hashmap
        '''

        prev_nums = {}

        for i in range(len(nums)):
            expected = target - nums[i]

            if expected in prev_nums:
                return [prev_nums[expected], i]
            else:
                prev_nums[nums[i]] = i
