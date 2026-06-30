class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        sortedNums = set(nums)
        for num in sortedNums:
            if num-1 not in sortedNums:
                length = 1
                while num+1 in sortedNums:
                    length+=1
                    num+=1
                longest = max(longest, length)

        return longest


        