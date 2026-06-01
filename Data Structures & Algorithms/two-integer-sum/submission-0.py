class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        allPrevNums = {} #this is storing the previous numbers we checked along
        #with its indexes
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in allPrevNums:
                return [allPrevNums[difference], i]
            allPrevNums[nums[i]] = i
        
        