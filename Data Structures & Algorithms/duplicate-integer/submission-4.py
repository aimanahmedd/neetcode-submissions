class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        input: array of integers numbers
        output: boolean

        so if a number appears more than once in the array, we need to return true
        if not just false. this problem is trying to find duplicates

        plan:
        brute force:
        go through entire list each number by number

        1. create an empty hashmap- key will be the number and the value will be
        frequency
        2. create a for loop that will go through each number
            2a. if it is in the hashmap, automatically return true
            2b. if not in hashmap, add to hashmap and keep value as 1
        3. return false as default because we were able to make it out of for loop
        '''
        allVals = {}
        for num in nums:
            if num in allVals:
                return True
            else:
                allVals[num] = 1
        return False
        