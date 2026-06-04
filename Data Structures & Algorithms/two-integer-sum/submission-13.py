class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        understand:
        return indexes (i and j) that nums[i] + nums[j] == target

        input: [3, 4, 5, 6] target = 7
        nums[0] + nums[1] = 7
        3 + 4  = 7
        output: [0, 1]

        there will always be an answer!
        there are negative numbers and array is between 2 and 1000

        match:
        hashmap - easy access and lookup, and we need to store old values! :)

        plan:
        1. create hashmap (this will track all previous values we have encountered)
        2. for loop w/ indices
            2a. answer = target - nums[i]
            2b. if answer in hashmap, return [i, hashmap[answer]]
            2c. if not in hashmap, store nums[i] in hashmap
        '''
        prevHash = {}

        for i in range(len(nums)):
            answer = target - nums[i]

            if answer in prevHash:
                return [prevHash[answer], i]
            else:
                prevHash[nums[i]] = i
        