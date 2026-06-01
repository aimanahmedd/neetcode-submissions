class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        allNums = {}

        for num in nums:
            if num in allNums:
                return True
            else:
                allNums[num] = 1
        return False

         