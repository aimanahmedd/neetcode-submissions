class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        input: integer array nums
        output: length of longest conseq sequuence

        element may or may not appear consec!

        [2, 20, 4, 10, 3, 4, 5]
        -> 4 (2, 3, 4, 5)

        [0, 3, 2, 5, 4, 6, 1, 1]
        -> 7 (do not consider any duplicates)
        0, 1, 2, 3, 4, 5, 6

        match:
            hashmap to keep track of prev numbers
        
        plan:
            1. put nums into a set to get rid of duplicates
            2. create a variable to keep trakc of longest length
            3. for num in nums:
                if num-1 not in nums:
                    length = 1
                    while num+1 in nums:
                        length+=1
                        num+=1
                    longest = max(longest, lenght)
            4. return longest
        '''
        newNums = set(nums)
        longestLength = 0

        for num in newNums:
            if num-1 not in newNums:
                length = 1
                while num+1 in newNums:
                    length+=1
                    num+=1
                longestLength = max(longestLength, length)
        return longestLength
        