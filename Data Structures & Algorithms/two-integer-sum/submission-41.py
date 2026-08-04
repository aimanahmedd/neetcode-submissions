class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        allPrev = {}

        for i in range(len(nums)):
            if target-nums[i] in allPrev:
                return [allPrev[target-nums[i]], i]
            else:
                allPrev[nums[i]] = i
        