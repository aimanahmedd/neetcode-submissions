class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        understand:
        [1, 2, 3, 3]
        true!

        [1, 2, 3, 4]
        false! :(

        input: array of numbers
        output: boolean

        match:
        hashmap: easily store previous values in the array and automatically check 
        if the value we are on is already in the hashmap
        super easy to lookup super to access we love hashmaps!

        plan:
        1. empy hashmap for previous numbers
        2. for num in nums for loop:
            2a. if num in hashmap return true
            2b. else add the number in hashmap
        3. return false
        '''

        prevNums = {}

        for num in nums:
            if num in prevNums:
                return True
            else:
                prevNums[num] = 1
        return False