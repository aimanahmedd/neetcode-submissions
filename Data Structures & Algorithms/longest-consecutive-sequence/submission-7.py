class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        understand:
        input: integer array of numbers
        output: LENGTH of the longest consecutive sequence

        [1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 16]
        answer = 7

        [] -> not possible! array length is 0 to 1000

        [2, 2, 2, 2] -> longest length = 0

        [2, 20, 4, 10, 3, 4, 5]
        output = 4
        2, 3, 4, 5
        -> duplicates do not count!

        [0, 3, 2, 5, 4, 6, 1, 1]
        output = 7
        0, 1, 2, 3, 4, 5, 6

        [0, 1, 2, 3, 4, 5, 6]

        match:
        array - use one for loop and slide through nums easily!


        plan:

        brute force:
        take the first index
        for i in range(len(nums))
            for nums[i+1]

        MAIN GOAL: length of longest sequence
        1. sort the array in order and get rid of any duplicates. use set function
        2. have an empty variable for both the longest and the length
        3. for num in ordered nums:
            3a. if num-1 not in order nums:
                length = 1
                while num+1 in ordered nums:
                    length+=1
                    num+=1
                longest = max(;ongest, length)
        4. return longest
        '''

        ordered_nums = set(nums)
        longest = 0

        for num in ordered_nums:
            if num-1 not in ordered_nums:
                length = 1
                while num+1 in ordered_nums:
                    length+=1
                    num+=1
                longest = max(length, longest)

        return longest      