class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ordered_nums = set(nums)
        longest_length = 0

        for num in ordered_nums:
            if num-1 not in ordered_nums:
                curr_length = 1
                while num+1 in ordered_nums:
                    curr_length +=1
                    num+=1
                longest_length = max(longest_length, curr_length)

        return longest_length
        