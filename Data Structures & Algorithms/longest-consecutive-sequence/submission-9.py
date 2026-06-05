class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        input: array of nums
        output: integer representing LENGTH of longest

        elements do not need to be in order!


        match:
        array (using a set)
        want to get rid of duplicates and keep numbers in order to understand sequence


        plan:
        1. create a set of nums so we can get rid of duplicate numbers and put the
        numbers in order
        2. create a variable to keep track of longest length
        3. for loop for num in nums:
            3a. if its the first number in the sequence:
                3a.a length = 1
                3a.b while num+1 in array:
                    length+=1
                longest = max (longest, length)
        return longest

        '''

        new_nums = set(nums)

        longest = 0

        for num in new_nums:
            if num-1 not in new_nums:
                length = 1
                while num+1 in new_nums:
                    length+=1
                    num+=1
                longest = max(longest, length)
        return longest