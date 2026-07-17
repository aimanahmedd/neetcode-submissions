class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
            understand:
            input: intger array of numbers
            output: boolean if a  number appears more than once

            [1, 2, 3, 3]
                -> true: 3 appears more than once

            [1, 2, 3, 4]
            -> false: no number appears more than once

            match:
                hashmap to keep track of numbers we already encounter

            plan:
                1. create empty hashmap to keep track of all numbers we encounter
                2. O(n) loop through array when we find something that has been in the array
                return true, else add to hashmap
        '''
        allNums = {}

        for num in nums:
            if num in allNums:
                return True
            else:
                allNums[num] = 1
        return False
        