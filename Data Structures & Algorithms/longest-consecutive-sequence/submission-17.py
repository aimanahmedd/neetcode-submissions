class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        understand:
        input = integer array of numbers
        output: longest consequtive sequence in array

        [2, 20, 4, 10, 3, 4, 5]
        4 -> 2, 3, 4, 5

        [0, 3, 2, 5, 4, 6, 1, 1]
        7 -> 0, 1, 2, 3, 4, 5, 6

        match:
            simple array

        plan:
            1. make variable longest_length = 0 (this will be what we return)
            2. make new nums that are sorted and removes duplicates
            3. for num in new nums:
                if num-1 in new nums:
                    continue
                
                length = 1
                while num+1 in newnums:
                    length+=1
                    num +=1
                longest_length = max(longest_length, length)
            rturn longest_length
        '''
        longest_length = 0

        new_nums = set(nums)

        for num in new_nums:
            if num-1 in new_nums:
                continue

            length = 1
            while num+1 in new_nums:
                length+=1
                num+=1
            longest_length = max(longest_length, length)
        return longest_length

        