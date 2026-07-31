class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        understand:
        input: integer array of numbers
        output: boolean if number appears more than once

        [1, 2, 3, 3]
        -> true (3 appears  more than once)

        [1,2, 3, 4]
        -> false (no number appears more than once)
        []

        match:
        use hashmap to keep track of prev indexes

        plan:
        1. create an empty hashmap that stores all previous numbers
        2. for num in nums
            if the num is in the hashmap return true
            else add number to hashmap
        3. return false
        '''

        prevNums = {}

        for num in nums:
            if num in prevNums:
                return True
            else:
                prevNums[num] = 1
        return False