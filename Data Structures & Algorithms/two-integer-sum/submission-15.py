class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevnums = {}

        for i in range(len(nums)):
            if target-nums[i] in prevnums:
                return [prevnums[target-nums[i]], i]
            else:
                prevnums[nums[i]] = i