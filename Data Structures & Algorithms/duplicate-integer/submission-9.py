class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        allPrev = {}

        for num in nums:
            if num in allPrev:
                return True
            else:
                allPrev[num] = 1
        return False
    
        