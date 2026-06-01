class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        understand:
        input: integer array can be in any order, numbers do not have to consecutive
        output: LENGTH of consecutive sequence

        can be duplicates BUT we should not consider it!
        numbers can be negative and postive very large!

        match:
            array - keep the numbers in an order and get rid of any duplicates

        plan:
            1.  make a set of the numbers to put them in order and get rid of duplicates
            2. make a variable for length and longest to keep track of largest consec
            3. for num in set:
                3a. while num + 1 in set
                    length increases by 1
                    num increases by 1
                3b. max between length and longest
            4. return longest

        [0, 3, 2, 5, 4, 6, 1, 1]

        [0, 1, 2, 3, 4, 5, 6]

        0



        [2, 20, 4, 10, 3, 4, 5]
        [2, 3, 4, 5, 10, 20]

        length = 3
        '''
        orderedSet = set(nums)
        longest = 0

        for num in orderedSet:
            if num-1 not in orderedSet:
                length = 1
                while num+1 in orderedSet:
                    length +=1
                    num+=1
                longest = max(length, longest)
        return longest

        