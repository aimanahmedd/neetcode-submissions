class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        understand:
        input: integer array nums
        output: length of the longest consec

        array between 0 and 100k

        match:
        arrays

        plan:
        1. create a variable to keep track of longest length = 0
        2. for num in nums:
            length = 1
            while num+1 in nums:
                length+=1 2, 3 4
                num+=1

            longestLength = max(longestLength, length)
        3. return longestLength
        '''
        longestLength = 0

        newNums = set(nums)
        #{2, 3, 4, 5, 10, 20}

        for num in newNums:
            if num-1 not in newNums:

                length = 1

                while num+1 in newNums:
                    length+=1
                    num+=1
            
                longestLength = max(longestLength, length)
        return longestLength