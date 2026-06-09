class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevNums = {}

        for num in nums:
            if num in prevNums:
                return True
            else:
                prevNums[num] = 1
        return False
        