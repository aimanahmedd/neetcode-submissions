class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        understand:
        input: integer array of numbers
        output: numbers, length of longest sequence

        [3, 4, 6, 7, 8, 5]
        output: 3

        edge cases:
        - if there are duplicated remove them
        - if one element it would just be 0 (no conseq sequence)

        plan:
        1. create a set of number for nums, so no duplicates and we know what to expect for
        number order
        2. create variable for longest sequence
        3. for num in set(nums):
            3a. if num-1  not in set:
                3b. length = 0
                3c. do a while loop to make sure the next number is in set and update
                length
            3d. find the max between length and longest
        4. return longest




        [2, 3, 4, 5, 10, 20]

        [0, 1, 2, 3, 4, 5, 6]
        '''
        orderedNumbers = set(nums)
        longestSequence = 0

        for num in orderedNumbers:
            if num-1 not in orderedNumbers:
                length = 1
                while num+1 in orderedNumbers:
                    length+=1
                    num+=1
                longestSequence = max(longestSequence, length)
        return longestSequence