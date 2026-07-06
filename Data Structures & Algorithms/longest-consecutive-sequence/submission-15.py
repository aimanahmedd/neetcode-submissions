class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length = 0

        orderedNums = set(nums)

        for num in orderedNums:
            if num-1 not in orderedNums:
                curr_length = 1
                
                while num+1 in orderedNums:
                    curr_length+=1
                    num+=1
                longest_length = max(longest_length, curr_length)

        return longest_length

                
        