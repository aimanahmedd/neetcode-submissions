class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        allNums = {}
        
        for num in nums:
            if num in allNums:
                allNums[num] = allNums[num] + 1
            else:
                allNums[num] = 1
        
        for key in allNums:
            if allNums[key] > 1:
                return True
        return False
            
         