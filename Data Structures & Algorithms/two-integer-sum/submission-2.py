class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        allPrevs = {}

        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in allPrevs:
                return [allPrevs[ans], i]
            else:
                allPrevs[nums[i]] = i