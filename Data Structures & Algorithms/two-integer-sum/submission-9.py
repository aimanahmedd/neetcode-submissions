class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Understand:
        -input: list of integers nums, and an integer target
        - output: a list of indices that their nums == target

        questions:
        - can there be a case with one number (no each input has the indices)
        - can there be a case with negative numbers (yest as long as they equal)

        edge cases:
        - two number list --> both indices (0, 1)

        runtime and complexity:
        O(n^2)

        Plan:
        1. hashmap to store previous numbers
        2. variable result for the answer
        3. use a for loop (the range length way)
            3a. do target - currentNum
                3a.a. if that num is in hashmap, add both indices into list and return
                3a. b if not in hashmap, add num and index in hashmap      
        '''

        allPrevNums = {} #all the previous numbers we encounter
        for i in range(len(nums)):
            if (target - nums[i] in allPrevNums):
                return [allPrevNums[target-nums[i]], i]
            else:
                allPrevNums[nums[i]] = i