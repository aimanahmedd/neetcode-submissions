class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            understand:
            input: integer array of numbers (random order)
            output: LENGTH of the longest consec sequence

            [2, 20, 4, 10, 3, 4, 5]

            [2, 3, 4, 5, 10, 20]

            output: 4
            (2, 3, 4, 5) is the longest sequence

            no considering duplicates!

            match:
                use a set to sort our the integer array of numbers
                to get rid of duplicates and put in order

            plan:
            1. make a variable for longest length and set it 0
            2. for num in num (no need for index):
                2a. if this is the first number in the sequence, make
                a variable to keep track of the length
                    2b. while num + 1 in the set, increase length and num
                
                    2c. check the longest against the length
            3. return longest variable
        '''

        longest = 0
        ordered_nums = set(nums)
        for num in ordered_nums:
            if num-1 not in ordered_nums:
                length = 1
                while num + 1 in ordered_nums:
                    length+=1
                    num+=1
                longest = max(longest, length)
        return longest
        