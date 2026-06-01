class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #putting our numbers in a set with not duplicates w O(1) time
        longestSeq = 0
        for num in numSet:
            if (num - 1) not in numSet:
                lengthOfSeq = 0
                while (num + lengthOfSeq) in numSet:
                    lengthOfSeq+=1
                longestSeq = max(longestSeq, lengthOfSeq)
        return longestSeq                
        