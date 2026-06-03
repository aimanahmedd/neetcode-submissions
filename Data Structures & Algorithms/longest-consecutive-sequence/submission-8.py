class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        understand:
        LENGTH of the longest consec sequence

        10, 11, 12
        1,2,3,4,5,6
        output:6 because that is the length of the longest sequence

        input: integer number array of nums
        output: integer representing the length

        in the case of an empty array: length would just be 0
        in the case we have an array with all the same numbers:
        [2, 2, 2, 2, 2]: length would be 1

        negatives are allowed! length between 0 and 1000

        match:
        no hashmap! we are doing O(n) time, BUT array and sets are allowed

        plan:
        1. empty variable for both the length (of the current sequecene we are on)
        and just have a variable longest (which represents longest length)
        2. create a set of the numbers to be able to get rid of duplicates and put 
        in order
        3. for num in nums:
            3a. if num-1 not in array:
                3a.a length = 1
                3a.b while num+1 in array"
                    3a.b.a length+=1
                    3a.b.b num+=1
                longest = max(longest, length)
        return longest

        [2, 20, 4, 10, 3, 4, 5]
        we do not consider duplicates!
        [2, 3, 4, 5, 10, 20]
        '''
        longest_seq = 0
        ordered_nums = set(nums)

        for num in ordered_nums:
            if num-1 not in ordered_nums:
                length = 1
                while num+1 in ordered_nums:
                    length+=1
                    num+=1
                longest_seq = max(longest_seq, length)
        return longest_seq
        