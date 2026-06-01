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
        
        '''basically the method to do this is first putting all the numbers in a set 
        for easy O(1) time that way we are easily able to check if it has a left or 
        a right. next is to iterate through our list of numbers and bsicall start out 
        by checkinf for if it is the first number in our sequence(does the number 
        right before it exist in the set). if it is start constructing the length of this
        sequence, and do this by continue chekcing if the the next number exists in the set.
        check if this sequence we just made is longer than the original variable. do this
        for all other numbers in the set
        '''